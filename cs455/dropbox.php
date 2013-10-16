<?php

# Include the Dropbox SDK libraries
require_once "dropbox-sdk/Dropbox/autoload.php";
use \Dropbox as dbx;

$appKey = 'tsyd07dln498sxc';
$appSecret = '5r5hayqqbzf7yrw';

if(isset($_GET['token_type'])) {
	echo $_GET['token'];
	/*
	echo "here i am ";
	$code = $_GET['code'];
	echo "$code";
	$fields = array(
		'code' => $code,
		'grant_type' => "authorization_code",
		'redirect_uri' => "http://localhost/cs455/cs455/dropbox.php",
		);

	foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
rtrim($fields_string, '&');

	curl_setopt($ch, CURLOPT_USERPWD, "$appKey:$appSecret");
	curl_setopt($ch,CURLOPT_POST, count($fields));
	curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);
	$url = "https://api.dropbox.com/1/oauth2/token";
	//echo $url;
	$ch = curl_init($url);

	curl_setopt($ch, CURLOPT_POST, true);
	//curl_setopt($ch, CURLOPT_GET, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$ret = curl_exec($ch);

	curl_close($ch);
	echo "heas".$ret."\n";
	//var_dump($ret);
	*/
} else {
/*
	get the values for $getDropBoxAuthenticated, $authcode.
*/
echo "here";

//$getDropBoxAuthenticated = true;
//$webAuth = new dbx\WebAuthRedirect($appInfo, "localhost/software/dropbox.php");

$csrf_token = new dbx\ArrayEntryStore($_SESSION, 'dropbox-auth-csrf-token');
$redirect_uri = 'http://localhost/cs455/cs455/dropbox1.php';
$authorizeURL = "https://www.dropbox.com/1/oauth2/authorize?client_id=$appKey&response_type=token&redirect_uri=$redirect_uri&state=";
echo $authorizeURL."\n";


header("Location: $authorizeURL");

}





/*if ($getDropBoxAuthenticated == true) {
	$authCode = "x22uT6fzw0wAAAAAAAAAAXMx2HOYRs9GtFZS2wAgN8A";	
} else {
	echo "1. Go to: " . "<a href = $authorizeUrl> $authorizeUrl </a>" . "\n";
	echo "2. Click \"Allow\" (you might have to log in first).\n";
	echo "3. Copy the authorization code.\n";
	$authCode = \trim(\readline("Enter the authorization code here: "));
}
list($accessToken, $dropboxUserId) = $webAuth->finish($authCode);
*/
/*print "Access Token: " . $accessToken . "\n";
print "";

$dbxClient = new dbx\Client($accessToken, "PHP-Example/1.0");
$accountInfo = $dbxClient->getAccountInfo();

print_r($accountInfo);

$f = fopen("working-draft.txt", "rb");
$result = $dbxClient->uploadFile("/working-draft.txt", dbx\WriteMode::add(), $f);
fclose($f);
print_r($result);

$folderMetadata = $dbxClient->getMetadataWithChildren("/");
print_r($folderMetadata);

$f = fopen("working-draft.txt", "w+b");
$fileMetadata = $dbxClient->getFile("/working-draft.txt", $f);
fclose($f);
print_r($fileMetadata);
*/
?>