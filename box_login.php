<?php /*session_start();
  $_SESSION['boxtoken']="dkdf";
  header("Location: home.php");*/
?>

<?php session_start();
// Include the Box_Rest_Client class
include('sdk/box-php-sdk/lib/Box_Rest_Client.php');
                      
// Set your API Key. If you have a lot of pages reliant on the 
// api key, then you should just set it statically in the 
// Box_Rest_Client class.
$api_key = 'mlwz4jl8zmb75ms6l6h56mo5r0w605cr';
$box_net = new Box_Rest_Client($api_key);

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
$_SESSION['boxtoken']=$box_net->auth_token;
//$_SESSION['boxclient']=$box_net;
echo $_SESSION['boxtoken']."\n";
//echo $_SESSION['boxclient']."\n";
//header("Location: home.php");
echo $box_net->auth_token."<br/>";
$folder = $box_net->folder(0); 
var_dump($folder->file);
?>
