<?php session_start();
// Include the Box_Rest_Client class
include('box-php-sdk-master/lib/Box_Rest_Client.php');
                      
// Set your API Key. If you have a lot of pages reliant on the 
// api key, then you should just set it statically in the 
// Box_Rest_Client class.
$api_key = '86slra9tek0b1gccb9iwy1ualyc2qqk5';
$box_net = new Box_Rest_Client($api_key);
         
//echo "here";

if(!array_key_exists('auth',$_SESSION) || empty($_SESSION['auth'])) {
  $_SESSION['auth'] = $box_net->authenticate();
  echo $_SESSION['auth']."<br/>";
}
else {
  // If the auth $_SESSION key exists, then we can say that 
  // the user is logged in. So we set the auth_token in 
  // box_net.
  $box_net->auth_token = $_SESSION['auth'];
  echo $_SESSION['auth']."<br/>";
} 
echo $box_net->auth_token."<br/>";
$folder = $box_net->folder(0); 
//var_dump($folder->file);
//echo "<br/>";
foreach ($folder->file as &$try) {
    var_dump($try);
    echo "<br/><br/>";
}
//var_dump($folder->file);
?>
