<!DOCTYPE html>
<html class="js js csstransitions" lang="en"><head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Open Source Workflow Software &amp; Business Process Management BPM</title>
        <meta http-equiv="Content-Language" content="en"><meta name="description" content="Open source web based workflow software and Business Process Management software">
             <meta name="keywords" content="workflow software"><meta name="googlebot" content="index, follow">
        <meta name="robots" content="index, follow">
        <meta name="Revisit-After" content="7 days">
        <meta name="city" content="Brooklyn">
        <meta name="country" content="United States of America (USA)">
        <meta name="state" content="NY">
        <meta name="zip code" content="11238">
        <meta name="geo.region" content="US-NY">
        <meta name="geo.placename" content="Brooklyn">
        <meta name="DC.title" content="ProcessMaker Inc.">
        <meta name="subject" content="Open Source Workflow, Business Process Management (BPM) Soft-ware.">
        <meta name="author" content="ProcessMaker Inc.">
        <meta name="copyright" content="ProcessMaker Inc.">        <link type="text/css" rel="stylesheet" href="index_files/css_xE-rWrJf-fncB6ztZfd2huxqgxu4WO-qwma6Xer30m4.css" media="all">
        <link type="text/css" rel="stylesheet" href="../css/general.css" media="all">
        <link type="text/css" rel="stylesheet" href="../css/sb-admin-2.css" media="all">
        <link rel="shortcut icon" href="http://www.processmaker.com/favicon.ico" type="image/vnd.microsoft.icon">
        <link rel="alternate" type="application/rss+xml" title="ProcessMaker RSS" href="http://www.processmaker.com/rss.xml">
        <script src="index_files/jsbox.js" class="lazyload" charset="utf-8"></script><script src="index_files/jsglobal.js" class="lazyload" charset="utf-8"></script><script src="index_files/jstrack.js" class="lazyload" charset="utf-8"></script><link type="text/css" rel="stylesheet" href="index_files/style_002.css" class="lazyload" charset="utf-8"><style type="text/css">.lz_chat_mail { color: #000000 !important; }.lz_chat_link { color: #000000 !important; }.lz_chat_file { color: #000000 !important; }.lz_chat_human { color: #000000 !important; }</style><link type="text/css" rel="stylesheet" href="index_files/style.css" class="lazyload" charset="utf-8"><script src="index_files/jsextern.js" class="lazyload" charset="utf-8"></script><style type="text/css">.fancybox-margin{margin-right:16px;}</style></head>
        <script>
            document.onreadystatechange = function () {
              var state = document.readyState
              if (state == 'interactive') {
                   document.getElementById('main-content').style.visibility="hidden";
              } else if (state == 'complete') {
                 document.getElementById('loading').style.visibility="hidden";
                 document.getElementById('loading').style.display="none";
                 document.getElementById('main-content').style.visibility="visible";
              }
            }
    </script>
    <body class="html front not-logged-in no-sidebars page-node" id="page-top" data-spy="scroll" data-target=".navbar-custom" style="background-color:white;">
    <div id="main-content" class="container" style="display:none;">
        <div class="row">
            <div class="col-lg-12" style="margin: 0 auto;">
                <div style="margin: 0 auto; width:600px;padding:25px;">
                        <div style="margin: 0 auto; text-align:center;margin-top:40px;">
                            <img src = "../images/logo-processmake-google.png">
                        </div>
                        <h2 style="margin: 0 auto; text-align:center; margin-top:40px;">ProcessMaker Google Integration</h2>
                        <p style="margin: 0 auto; text-align:center; margin-top:10px;">
                            The ProcessMaker Google Integration extension and components have been uninstalled from your Gmail Acccount.
                        </p>
                </div>

            </div>
        </div>
    </div>

    <div id="loading" style="width:120px;margin:0 auto;margin-top:200px;text-align:center;">
        <img id="loading-image" src="../images/ext/default/shared/large-loading.gif" alt="Uninstalling..." />
        <div>Uninstalling ...</div>
    </div>  
    </body>
</html>


<?php
/*
* Uninstall file to help in the uninstaling process of the PMGmail Extension. 
* This deletes the labels created by the Extension in the user email.
*
*/
/**
 * Call the end point to delete labels
 *
 * @param string $server
 * @param string $pmws
 * @param string $mail
 * @param string $pmtoken
 */
function callEndPointDeleteLabels($server, $pmws, $mail, $pmtoken){
    set_time_limit(60);

    $curl = curl_init( 'https://' . $server . '/api/1.0/' . $pmws . '/gmailIntegration/deleteLabels/'. $mail );
    curl_setopt( $curl, CURLOPT_HTTPHEADER, array( 'Authorization: Bearer ' . $pmtoken ) );
    curl_setopt( $curl, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt( $curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt( $curl, CURLOPT_CONNECTTIMEOUT, 0);

    $curl_response = curl_exec( $curl );
    curl_close($curl);
}

$server = $_GET['server'];
$pmws = $_GET['pmws'];
$mail = $_GET['mail'];
$pmtoken = $_GET['pmtoken'];

callEndPointDeleteLabels($server, $pmws, $mail, $pmtoken);
?>
