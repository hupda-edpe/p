<?php

/**
 * pmGmail controller
 * @inherits Controller
 *
 * @access public
 */

class pmGmail extends Controller
{
    public function saveConfigPmGmail($httpData)
    {
        G::LoadClass( "pmGoogleApi" );
        $pmGoogle = new PMGoogleApi();
        $result = new StdClass();
        $result->success = true;

        if (!empty($httpData->status_pmgmail)) {
            $httpData->status_pmgmail = $httpData->status_pmgmail == 1 ? true : false;
            $pmGoogle->setStatusService($httpData->status_pmgmail);
            $message = G::LoadTranslation('ID_ENABLE_PMGMAIL') . ': ' . ($httpData->status_pmgmail ? G::LoadTranslation('ID_ENABLE') : G::LoadTranslation('ID_DISABLE'));

            $pmGoogle->setTypeAuthentication($httpData->typeAuth);

            if (!empty($httpData->email_service_account)) {
                $pmGoogle->setServiceAccountEmail($httpData->email_service_account);
                $message .= ', ' . G::LoadTranslation('ID_PMG_EMAIL') . ': ' . $httpData->email_service_account;
            }
            if (!empty($_FILES)) {
                if (!empty($_FILES['file_p12']) && $_FILES['file_p12']['error'] != 1) {
                    if ($_FILES['file_p12']['tmp_name'] != '') {
                        G::uploadFile($_FILES['file_p12']['tmp_name'], PATH_DATA_SITE, $_FILES['file_p12']['name']);
                        $pmGoogle->setServiceAccountP12($_FILES['file_p12']['name']);
                        $message .= ', ' . G::LoadTranslation('ID_PMG_FILE') . ': ' . $_FILES['file_p12']['name'];
                    }
                } else if (!empty($_FILES['file_json']) && $_FILES['file_json']['error'] != 1) {
                    if ($_FILES['file_json']['tmp_name'] != '') {
                        G::uploadFile($_FILES['file_json']['tmp_name'], PATH_DATA_SITE, $_FILES['file_json']['name']);
                        $pmGoogle->setAccountJson($_FILES['file_json']['name']);
                        $message .= ', ' . G::LoadTranslation('ID_PMG_FILE') . ': ' . $_FILES['file_json']['name'];
                    }
                } else {
                    $result->success = false;
                    $result->fileError = true;
                    print(G::json_encode($result));
                    die();
                }
            }
        } else {
            $pmGoogle->setStatusService(false);
            $message = G::LoadTranslation('ID_ENABLE_PMGMAIL') . ': ' . G::LoadTranslation('ID_DISABLE');
        }
        G::auditLog("Update Settings Gmail", $message);

        print(G::json_encode($result));
    }

    public function formPMGmail()
    {
        try {
            $this->includeExtJS('admin/pmGmail');
            if (!empty ($_SESSION['__PMGMAIL_ERROR__'])) {
                $this->setJSVar('__PMGMAIL_ERROR__', $_SESSION['__PMGMAIL_ERROR__']);
                unset($_SESSION['__PMGMAIL_ERROR__']);
            }
            G::LoadClass( "pmGoogleApi" );
            $pmGoogle = new PMGoogleApi();
            $accountEmail = $pmGoogle->getServiceAccountEmail();
            $fileP12 = $pmGoogle->getServiceAccountP12();
            $fileJson = $pmGoogle->getAccountJson();
            $fileJson = $fileJson == null ? '' : $fileJson;
            $type = $pmGoogle->getTypeAuthentication();
            $enablePMGmail = $pmGoogle->getStatusService();

            $this->setJSVar('accountEmail', $accountEmail);
            $this->setJSVar('fileP12', $fileP12);
            $this->setJSVar('enablePMGmail', $enablePMGmail);
            $this->setJSVar('fileJson', $fileJson);
            $this->setJSVar('typeAuthentication', $type);


            G::RenderPage('publish', 'extJs');
        } catch (Exception $error) {
            $_SESSION['__PMGMAIL_ERROR__'] = $error->getMessage();
            die();
        }
    }

    /**
     * @param $httpData
     */
    public function testConfigPmGmail($httpData)
    {
        G::LoadClass( "pmGoogleApi" );
        $pmGoogle = new PMGoogleApi();

        $result = new stdClass();

        $result->typeAuth = empty($httpData->typeAuth) ? $pmGoogle->getTypeAuthentication() : $httpData->typeAuth;
        if ($result->typeAuth == 'webApplication') {
            $result->pathFileJson = empty($_FILES['file_json']['tmp_name']) ? PATH_DATA_SITE . $pmGoogle->getAccountJson() : $_FILES['file_json']['tmp_name'];
        } else {
            $result->emailServiceAccount = empty($httpData->email_service_account) ? $pmGoogle->getServiceAccountEmail() : $httpData->email_service_account;
            $result->pathServiceAccountP12 = empty($_FILES['file_p12']['tmp_name']) ? PATH_DATA_SITE . $pmGoogle->getserviceAccountP12() : $_FILES['file_p12']['tmp_name'];
        }

        print(G::json_encode($pmGoogle->testService($result)));
    }

    /**
     *
     */
    public function testUserGmail()
    {
        $criteria = new Criteria();
        $criteria->clearSelectColumns();
        $criteria->addSelectColumn('COUNT(*) AS NUM_EMAIL');
        $criteria->addSelectColumn(UsersPeer::USR_UID);
        $criteria->addSelectColumn(UsersPeer::USR_FIRSTNAME);
        $criteria->addSelectColumn(UsersPeer::USR_LASTNAME);
        $criteria->addSelectColumn(UsersPeer::USR_EMAIL);
        $criteria->addGroupByColumn(UsersPeer::USR_EMAIL);

        $rs = UsersPeer::doSelectRS($criteria);
        $rs->setFetchmode(ResultSet::FETCHMODE_ASSOC);

        $userRepeat = array();
        while ($rs->next()) {
            $row = $rs->getRow();
            if ($row['NUM_EMAIL'] > 1) {
                $userRepeat[] = array(
                    'USR_UID' => $row['USR_UID'],
                    'FULL_NAME' => $row['USR_FIRSTNAME'] . ' ' . $row['USR_LASTNAME'],
                    'EMAIL' => $row['USR_EMAIL']
                );
            }
        }

        print(G::json_encode($userRepeat));
    }
}
