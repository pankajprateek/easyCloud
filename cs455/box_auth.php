<html>


<?php
	session_start();
	include('box-php-sdk-master/lib/Box_Rest_Client.php');
	
	$api_key = '86slra9tek0b1gccb9iwy1ualyc2qqk5';
	$box_net = new Box_Rest_Client($api_key);
	
	if(!array_key_exists('box_auth',$_SESSION) || empty($_SESSION['box_auth'])) {
		$_SESSION['box_auth'] = $box_net->authenticate();			
		//var_dump($_SESSION);
		//header("Location: box_auth.php");
	}
	else {	
		$box_net->auth_token = $_SESSION['box_auth'];		
		header("Location: main.php");
	}
	
?>
</html>