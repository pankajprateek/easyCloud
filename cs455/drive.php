<?php
session_start();
class Drive {

	public $client;
	public $service;

	function __construct() {
		require_once 'google-api-php-client/src/Google_Client.php';
		require_once 'google-api-php-client/src/contrib/Google_DriveService.php';
		$this->client = new Google_Client();
		$this->client->setClientId('1057221066577-tk81bpa02v8k1hbokp3sampjkgeh1ee2.apps.googleusercontent.com');
		$this->client->setClientSecret('CX7WZ7uJOuSD2pYB68ZnkoGk');
		$this->client->setRedirectUri('http://localhost/cs455/cs455/drive.php');
		$this->client->setScopes(array('https://www.googleapis.com/auth/drive'));

		$this->service = new Google_DriveService($this->client);
		if (isset($_SESSION['driveId'])) {			
			$accessToken = $_SESSION['driveId'];
			$this->client->setAccessToken($accessToken);
		}
	}

	public static function isAuthenticated() {
		if (isset($_SESSION['driveId'])) {
			return true;
		}	
		return false;
	}

	public function getAuthToken() {
		return $this->client->getAccessToken();
	}
	
	public function getFolder() {
		$files = $this->service->files->listFiles($parameters);
		$items = $files["items"];

		$output = array();
		foreach($items as $i) {
			//var_dump($i);
			
			//echo $i["modifiedDate"]." ".$i["kind"].$nl.$nl;
			$output[] = array("path" => $i["title"],  "is_dir" => 0, "stored_at" => "Drive", "last_modified" => $i['modifiedDate']);
		}
		return $output;
	}
}
?>