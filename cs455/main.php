<?php

session_start();

require_once 'drive.php';

$nl = "\n<br>";
$drive = new Drive();
$client = $drive->client;
$service = $drive->service;
echo $drive->getAuthToken().$nl.$nl;

//Insert a file
$file = new Google_DriveFile();
$file->setTitle('My document');
$file->setDescription('A test document');
$file->setMimeType('text/plain');

$data = file_get_contents('document.txt');

echo $data."\n";

$createdFile = $service->files->insert($file, array(
      'data' => $data,
      'mimeType' => 'text/plain',
    ));

print_r($createdFile);
?>