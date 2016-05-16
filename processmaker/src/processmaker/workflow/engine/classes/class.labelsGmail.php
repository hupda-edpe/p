<?php

class labelsGmail
{
    function listLabels($service)
    {
        $labels = array();
        try {
            $labelsResponse = $service->users_labels->listUsersLabels('me');
            if ($labelsResponse->getLabels()) {
                $labels = array_merge($labels, $labelsResponse->getLabels());
            }
        } catch (Exception $e) {
            print G::LoadTranslation("ID_PMGMAIL_GENERAL_ERROR") . $e->getMessage();
        }
        return $labels;
    }

    /**
     * Modify the Labels a Message is associated with.
     *
     * @param  Google_Service_Gmail $service Authorized Gmail API instance.
     * @param  string $userId User's email address. The special value 'me'
     * can be used to indicate the authenticated user.
     * @param  string $messageId ID of Message to modify.
     * @param  array $labelsToAdd Array of Labels to add.
     * @param  array $labelsToRemove Array of Labels to remove.
     */
    function modifyMessage($service, $userId, $messageId, $labelsToAdd, $labelsToRemove) {
        $mods = new Google_Service_Gmail_ModifyMessageRequest();
        $mods->setAddLabelIds($labelsToAdd);
        $mods->setRemoveLabelIds($labelsToRemove);
        try {
            $message = $service->users_messages->modify($userId, $messageId, $mods);
        } catch (Exception $e) {
            print G::LoadTranslation("ID_PMGMAIL_GENERAL_ERROR") . $e->getMessage();
        }
    }

    /**
     * Get list of Messages in user's mailbox.
     *
     * @param  Google_Service_Gmail $service Authorized Gmail API instance.
     * @param  string $userId User's email address. The special value 'me'
     * can be used to indicate the authenticated user.
     * @return array Array of Messages.
     */
    function listMessages($service, $userId, $query, $labels) {
        $pageToken = NULL;
        $messages = array();
        $opt_param = array();
        do {
            try {
                if ($pageToken) {
                    $opt_param['pageToken'] = $pageToken;
                }
                $opt_param['labelIds'] = $labels;
                $opt_param['q'] = $query;
                $opt_param['maxResults'] = 3;
                $messagesResponse = $service->users_messages->listUsersMessages($userId, $opt_param);
                if ($messagesResponse->getMessages()) {
                    $messages = array_merge($messages, $messagesResponse->getMessages());
                }
            } catch (Exception $e) {
                print G::LoadTranslation("ID_PMGMAIL_GENERAL_ERROR") . $e->getMessage();
            }
        } while ($pageToken);

        return $messages;
    }

   public function setLabelsToPauseCase ($caseId, $index) {
       require_once PATH_TRUNK . 'vendor' . PATH_SEP . 'google' . PATH_SEP . 'apiclient' . PATH_SEP . 'src' . PATH_SEP . 'Google' . PATH_SEP . 'autoload.php';
       require_once (PATH_HOME . "engine" . PATH_SEP . "classes" . PATH_SEP . "class.pmGoogleApi.php");

       $Pmgmail = new \ProcessMaker\BusinessModel\Pmgmail();
       $appData = $Pmgmail->getDraftApp($caseId, $index);

       foreach ($appData as $application){
           $appNumber = $application['APP_NUMBER'];
           $index = $application['DEL_INDEX'];
           $threadUsr = $application['USR_UID'];
           $proName = $application['APP_PRO_TITLE'];
           $threadStatus = $application['DEL_THREAD_STATUS'];
           $appStatus = $application['APP_STATUS'];
       }

       //Getting the privious User email
       $oUsers = new \Users();
       $usrData = $oUsers->loadDetails($threadUsr);
       $mail = $usrData['USR_EMAIL'];

       //The Subject to search the email
       $subject = "[PM] " .$proName. " Case: ". $appNumber;

       $pmGoogle = new PMGoogleApi();
       $pmGoogle->setUser($mail);
       $pmGoogle->setScope('https://www.googleapis.com/auth/gmail.modify');
       $client = $pmGoogle->serviceClient();
       $service = new Google_Service_Gmail($client);
       $labelsIds = $this->getLabelsIds($service);

       if($appStatus == 'DRAFT'){
           $labelsToRemove = $labelsIds['Draft'];
           $labelsToSearch = "*-draft";
           $labelsToAdd = $labelsIds['Paused'];
       }

       if($appStatus == 'TO_DO'){
           $labelsToRemove = $labelsIds['Inbox'];
           $labelsToSearch = "*-inbox";
           $labelsToAdd = $labelsIds['Paused'];
       }

       $q = "subject:('".preg_quote($subject, '-')."') label:('".$labelsToSearch."')";
       $messageList = $this->listMessages($service, $mail, $q, $labelsToRemove);
       foreach ($messageList as $message) {
           $messageId = $message->getId();
           $modifyResult = $this->modifyMessage($service, $mail, $messageId, array($labelsToAdd), array($labelsToRemove));
       }
   }

    function setLabelsTounpauseCase ($caseId, $index) {
        require_once PATH_TRUNK . 'vendor' . PATH_SEP . 'google' . PATH_SEP . 'apiclient' . PATH_SEP . 'src' . PATH_SEP . 'Google' . PATH_SEP . 'autoload.php';
        require_once (PATH_HOME . "engine" . PATH_SEP . "classes" . PATH_SEP . "class.pmGoogleApi.php");

        $Pmgmail = new \ProcessMaker\BusinessModel\Pmgmail();
        $appData = $Pmgmail->getDraftApp($caseId, $index);

        foreach ($appData as $application){
            $appNumber = $application['APP_NUMBER'];
            $index = $application['DEL_INDEX'];
            $threadUsr = $application['USR_UID'];
            $proName = $application['APP_PRO_TITLE'];
            $threadStatus = $application['DEL_THREAD_STATUS'];
            $appStatus = $application['APP_STATUS'];
        }

        //Getting the privious User email
        $oUsers = new \Users();
        $usrData = $oUsers->loadDetails($threadUsr);
        $mail = $usrData['USR_EMAIL'];

        //The Subject to search the email
        $subject = "[PM] " .$proName. " Case: ". $appNumber;

        $pmGoogle = new PMGoogleApi();
        $pmGoogle->setUser($mail);
        $pmGoogle->setScope('https://www.googleapis.com/auth/gmail.modify');
        $client = $pmGoogle->serviceClient();
        $service = new Google_Service_Gmail($client);
        $labelsIds = $this->getLabelsIds($service);

        if($appStatus == 'DRAFT'){
            $labelsToRemove = $labelsIds['Paused'];
            $labelsToSearch = "*-paused";
            $labelsToAdd = $labelsIds['Draft'];
        }

        if($appStatus == 'TO_DO'){
            $labelsToRemove = $labelsIds['Paused'];
            $labelsToSearch = "*-paused";
            $labelsToAdd = $labelsIds['Inbox'];
        }

        $q = "subject:('".preg_quote($subject, '-')."') label:('".$labelsToSearch."')";
        $messageList = $this->listMessages($service, $mail, $q, $labelsToRemove);
        foreach ($messageList as $message) {
            $messageId = $message->getId();
            $modifyResult = $this->modifyMessage($service, $mail, $messageId, array($labelsToAdd), array($labelsToRemove));
        }
    }

   public function setLabels($caseId, $index, $actualLastIndex, $unassigned=false){
        //First getting the actual thread data
        $Pmgmail = new \ProcessMaker\BusinessModel\Pmgmail();
        $appData = $Pmgmail->getDraftApp($caseId, $index);

        foreach ($appData as $application){
            $appNumber = $application['APP_NUMBER'];
            $index = $application['DEL_INDEX'];
            $threadUsr = $application['USR_UID'];
            $proName = $application['APP_PRO_TITLE'];
            $threadStatus = $application['DEL_THREAD_STATUS'];
            $appStatus = $application['APP_STATUS'];
        }

        if($threadStatus == 'CLOSED' || $unassigned == true) {
            //Getting the privious User email
            $oUsers = new \Users();

            $usrData = $oUsers->loadDetails($threadUsr);
            $mail = $usrData['USR_EMAIL'];

            //The Subject to search the email
            $subject = "[PM] " .$proName. " Case: ". $appNumber;

            require_once PATH_TRUNK . 'vendor' . PATH_SEP . 'google' . PATH_SEP . 'apiclient' . PATH_SEP . 'src' . PATH_SEP . 'Google' . PATH_SEP . 'autoload.php';
            require_once (PATH_HOME . "engine" . PATH_SEP . "classes" . PATH_SEP . "class.pmGoogleApi.php");
            $pmGoogle = new PMGoogleApi();

            $pmGoogle->setUser($mail);

            $pmGoogle->setScope('https://www.googleapis.com/auth/gmail.modify');
            $client = $pmGoogle->serviceClient();

            $service = new Google_Service_Gmail($client);
            $labelsIds = $this->getLabelsIds($service);

            if($actualLastIndex == 0){
                $labelsToRemove = $labelsIds['Draft'];
                $labelsToSearch = "*-draft";
                $labelsToAdd = $labelsIds['Participated'];
            } else if ( ($actualLastIndex == -1) && ($unassigned == true) ){ //Unassigned
                $labelsToRemove = $labelsIds['Unassigned'];
                $labelsToSearch = "*-unassigned";
                $labelsToAdd = $labelsIds['Inbox'];
            } else if($actualLastIndex >= 1) {
                $labelsToRemove = $labelsIds['Inbox'];
                $labelsToSearch = "*-inbox";
                $labelsToAdd = $labelsIds['Participated'];
            }

            //Searching the email in the user's mail
            $q = "subject:('".preg_quote($subject, '-')."') label:('".$labelsToSearch."')";

            $messageList = $this->listMessages($service, $mail, $q, $labelsToRemove);

            foreach ($messageList as $message) {
                $messageId = $message->getId();

                $modifyResult = $this->modifyMessage($service, $mail, $messageId, array($labelsToAdd), array($labelsToRemove));

            }
        }
    }
    
    /**
     * Delete Label with given ID.
     *
     * @param  Google_Service_Gmail $service Authorized Gmail API instance.
     * @param  string $userId User's email address. The special value 'me'
     * can be used to indicate the authenticated user.
     * @param  string $labelId Id of Label to be updated.
     */
    public function deleteLabel($service, $user, $labelId)
    {
    	try {
    		$service->users_labels->delete($user, $labelId);
    	} catch (Exception $e) {
    		error_log(G::LoadTranslation("ID_PMGMAIL_GENERAL_ERROR") . $e->getMessage());
    	}
    }
    
    /**
     * Delete PMGmail integration labels getting the list of labels in an email account.
     * @param string $mail User mail adress.
     *
     */
    public function deletePMGmailLabels($mail)
    {
    	require_once (PATH_HOME . "engine" . PATH_SEP . "classes" . PATH_SEP . "class.pmGoogleApi.php");
    	$pmGoogle = new PMGoogleApi();
    
    	$pmGoogle->setUser($mail);
    
    	$pmGoogle->setScope('https://www.googleapis.com/auth/gmail.modify');
    	$client = $pmGoogle->serviceClient();
    
    	$service = new Google_Service_Gmail($client);
    	$count = 0;
    	$listlabels = $this->listLabels($service);
    	foreach ($listlabels as $label) {
    		if ($label->getName() == '* Inbox' ||
    				$label->getName() == '* Participated' ||
    				$label->getName() == '* Unassigned' ||
    				$label->getName() == '* Draft' ||
    				$label->getName() == '* Inbox' ||
    				$label->getName() == '*-- ProcessMaker --*' ||
    				$label->getName() == '* Paused'
    		) {
    			$oresp = $this->deleteLabel($service, 'me', $label->getId());
    			$count++;
    		}
    	}
    	return $count . ' labels successfully deleted.';
    }


    private function getLabelsIds($service) {
        $result = array();
        $listlabels = $this->listLabels($service);
        foreach ($listlabels as $label) {
            $labId =  $label->getId();
            $labName = $label->getName();
            switch($labName){
                case "* Inbox":
                    $result['Inbox'] = $labId;
                    break;
                case "* Participated":
                    $result['Participated'] = $labId;
                    break;
                case "* Unassigned":
                    $result['Unassigned'] = $labId;
                    break;
                case "* Draft":
                    $result['Draft'] = $labId;
                    break;
                case "* Paused":
                    $result['Paused'] = $labId;
                    break;
            }
        }
        return $result;
    }
}

