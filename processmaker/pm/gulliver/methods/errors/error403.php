<?php

$http = (isset($_SERVER["HTTPS"]) && $_SERVER["HTTPS"] == "on")? "https" : "http";
$host = $_SERVER["SERVER_NAME"] . (($_SERVER["SERVER_PORT"] != "80")? ":" . $_SERVER["SERVER_PORT"] : "");

$urlLogin = $http . "://" . $host . "/sys/en/neoclassic/login/login";
$urlHome =  $urlLogin;

if (isset($_GET["url"]) && $_GET["url"] != "") {
    $url = urldecode($_GET["url"]);
    $url = explode("/", $url);

    $sysSys = "";
    $sysLang = "";
    $sysSkin = "";

    if (isset($url[1]) && preg_match("/^sys(.+)$/", $url[1], $match)) {
        $sysSys = $match[1];
    }

    if (isset($url[2])) {
        $sysLang = $url[2];
    }

    if (isset($url[3])) {
        $sysSkin = $url[3];
    }

    if ($sysSys != "" && $sysLang != "" && $sysSkin != "") {
        $urlLogin = $http . "://" . $host . "/sys" . $sysSys . "/" . $sysLang . "/" . $sysSkin . "/login/login";
        $urlHome =  $http . "://" . $host . "/sys" . $sysSys . "/" . $sysLang . "/" . $sysSkin . "/cases/main";
    }
}

?>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <link rel="shortcut icon" href="/images/favicon.ico" type="image/x-icon"/>
  <link href="style1.css" type="text/css" rel="stylesheet"/>
</head>
<body style="margin: 0px; overflow: auto; background: url(images/background1.jpg); no-repeat; top;">
	<!-- Warp around everything -->
	<div id="warp">


		<!-- Header top -->
		<div id="header_top"></div>
		<!-- End header top -->


  <!-- Header -->
  <div id="header">
      <table border="0" cellspacing="0" cellpadding="0" width="90%">
          <tr>
              <td align="center">
                  <h2>Access denied!</h2>
                  <h5>Somebody prohibited this page, or the URL is incorrect.</h5>
              </td>
          </tr>
      </table>
  </div>
  <!-- End Header -->


		<!-- The content div -->
		<div id="content">

			<!-- text -->
			<div id="text">
				<!-- The info text -->
				<strong>Possible reasons: </strong>
<ul id="textInfo">
<li>The link is broken. This may occur when you receive a link via email but your client software adds line breaks, thus distorting long URLs.</li>
<li>The page you requested is no longer active.</li>
<li>There is a spelling mistake in the link, in case you entered the URL into the browser's address toolbar.</li>
</ul>
<ul>
				<br/>
				<h3>What you can do?</h3>
				<!-- End info text -->
				<br/>
    <!-- Page links -->
    <ul id="textInfo">
        <li>You might try retyping the URL and trying again.</li>
        <li>Or we could take you back to the <a href="<?php echo $urlHome; ?>">home page.</a></li>
        <li>Or you could start again from the <a href="<?php echo $urlLogin; ?>">login page.</a></li>
    </ul>
    <!-- End page links -->
			</div>
			<!-- End info text -->


			<!-- Book icon -->
			<img id="book" src="images/img-02.png" alt="Book iCon" />
			<!-- End Book icon -->

			<div style="clear:both;"></div>
		</div>
		<!-- End Content -->


  <!-- Footer -->
  <div id="footer" style="padding-top: 10px; color: #878787; font-size: 10px; text-align: center;">
      <span>&#169; Copyright 2000 - <?php echo date("Y"); ?> </span>
  </div>
  <!-- End Footer -->


		<!-- Footer bottom -->
		<div id="footer_bottom"></div>
		<!-- End Footer bottom -->


		<!-- Social Media list -->


		<!-- End Social media -->
		<div style="clear:both;"></div>


	  </div>
	<!-- End Warp around everything -->

  </div>
</body>
</html>