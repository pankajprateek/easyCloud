<!DOCTYPE HTML>
<html>
	<head>
		<meta charset = "utf8">
		<title>Cloud Storage Simplified</title>
		<link rel="stylesheet" href="bootstrap/css/bootstrap.css"  type="text/css"/>
		<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
		<script src="bootstrap/js/bootstrap.js"></script>
	</head>
	<body>
		<div class = "container">
			<div class = "row"> 
			<div class = "span2">
				<br><br>
				<div><a href = "drive_auth.php"> <img src="drive.jpg" height = "75px" width = "75px"/> </a></div> <br>
				<?php
					session_start();

					require_once 'drive.php';
					require_once 'Dropbox.class.php';
					require_once 'box_class.php';
					require_once 'easy_cloud.php';
			
					$dropbox = new Dropbox();
					$userArray = $dropbox->get('https://api.dropbox.com/1/account/info');
					echo '<div><a href="'.$dropbox->getAccessURL().'"><img src="dropbox.png" height = "75px" width = "75px"/></a></div> <br>';
				?>				
				<div><a href = "box_auth.php"> <img src="box.jpg" height = "75px" width = "75px"/> </a></div>		
			</div>
			<div class = "span10">
			<?php

			
			
			
			
			if(isset($_GET['auth_token'])) {
				$_SESSION['box_auth'] = $_GET['auth_token'];
			}
				
			$nl = "\n<br>";
			
			$output_drive = array();
			$output_box = array();
			$output_dropbox = array();
			
			if(Drive::isAuthenticated()) {
				$drive = new Drive();		
				$output_drive = $drive->getFolder();
			}
						
			if(Box::isAuthenticated()) {
				$box = new Box();							
				$box->getAuthenticated();			
				$output_box = $box->getFolder();
			}
			
			//$dropbox = new Dropbox();
			if($dropbox->hasAccess()) {
				$output_dropbox = $dropbox->getFolder('root', NULL);
			}
			
			$concatenated_arr = $output_dropbox;
			
			foreach($output_box as $ob) {
				$concatenated_arr[] = $ob;
			}
			foreach($output_drive as $od) {
				$concatenated_arr[] = $od;
			}									
			
			echo $nl.$nl;
			echo EasyCloud::getHTML($concatenated_arr);
			
			
			
			//echo $drive->getAuthToken().$nl.$nl;

			//Insert a file
			/*
			$file = new Google_DriveFile();			
			$file->setTitle('My document');
			$file->setDescription('A test document');
			$file->setMimeType('text/plain');
			*/
			//$data = file_get_contents('document.txt');

			//echo $data."\n";

			/*$createdFile = $service->files->insert($file, array(
				'data' => $data,
				'mimeType' => 'text/plain',
				));

			print_r($createdFile);
			*/


			
			?>
			</div>
			</div>
		</div>
	</body>
</html>
		