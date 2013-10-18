<?php

class Box{

	private $box_net;
	public function __construct() {
		include('box-php-sdk-master/lib/Box_Rest_Client.php');
		$api_key = '86slra9tek0b1gccb9iwy1ualyc2qqk5';
		$this->box_net = new Box_Rest_Client($api_key);
	}
	
	public static function isAuthenticated() {
		if(isset($_SESSION["box_auth"])) {	
			return true;
		}
		return false;
	}
	
	public function getAuthenticated() {
		if(isset($_SESSION["box_auth"])) {
			$this->box_net->auth_token = $_SESSION["box_auth"];
			//var_dump($_SESSION);
		}
	}
	
	public function getFolder() {
		$folder = $this->box_net->folder(0); 
		//var_dump($folder);
		$arr = array();
		foreach ($folder->file as $try) {
			//var_dump($try);
			$t = (array)$try;       
			foreach($t as $k => $v) {
				//var_dump($v);
				if($v['file_name']) {
					$arr[] = array("path" => $v['file_name'], "is_dir" => $v['is_dir'], "last_modified" => $v["updated"], "stored_at" => "Box.net");
				}		
			}    		
		}
		return $arr;
	}		
}


?>
