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
			<?php

			session_start();

			require_once 'drive.php';
			require_once '../software/dropbox/Dropbox.class.php';

			$nl = "\n<br>";
			$drive = new Drive();
			$client = $drive->client;
			$service = $drive->service;
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
			//echo $nl.$nl;

			$files = $service->files->listFiles($parameters);
			$items = $files["items"];

			$output = array();
			foreach($items as $i) {
				//var_dump($i);
				
				//echo $i["modifiedDate"]." ".$i["kind"].$nl.$nl;
				$output[] = array("path" => $i["title"],  "is_dir" => 0, "stored_at" => "Drive", "last_modified" => $i['modifiedDate']);
			}
			
			$dropbox = new Dropbox();
			echo $nl.$nl;
			echo $dropbox->getHTML($output);
			
			?>
		</div>
	</body>
</html>
		