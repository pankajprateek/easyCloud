  <!DOCTYPE HTML>
<html>
      <head>
	      <meta charset = "utf8">
	      <title>Cloud Storage Simplified</title>
	      <link rel="stylesheet" href="../../cs455/bootstrap/css/bootstrap.css"  type="text/css"/>
	      <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
	      <script src="../../cs455/bootstrap/js/bootstrap.js"></script>
      </head>
      <body>

	<div class = "container">

	      <?php

	      require_once 'Dropbox.class.php';

	      $dropbox = new Dropbox();

	      $userArray = $dropbox->get('https://api.dropbox.com/1/account/info');

	      $try = $dropbox->test('dropbox');
	      //echo $try;

	      //var_dump($dropbox->getFile('dropbox', 'Codes/dijkstra.cpp'));
	      //echo "<br>";
	      $nl = "<br>\n";

	      $arr = $dropbox->getFolder('root', NULL);
	      //var_dump($arr);
	      echo $dropbox->getHTML($arr);

	      /*
	      foreach($arr as $a) {
		//var_dump($a);
		echo $nl.$nl;
		if($a['is_dir'] == 1) {
		  echo "<a href = ''>".$a['path']." ".$a['is_dir']. "</a>".$nl;
		} else {
		  echo $a['path']." ".$a['is_dir']. $nl;
		}
		
	      }
	      */

	      /*
	      foreach ($meta as $key => $value) {
		  echo $key.$nl;
		  if($key == 'contents') {
		  
		  $a = (array)$value['0'];
		  var_dump($a);
		  echo $a['path'];
		  echo $nl;
		  $array[] = $a['path'];
		  }
	      }
	      */


	      //var_dump($meta['contents']);



	      ?>
	</div>
	<h1>Dropbox API</h1>
	
	<?php 
	if($dropbox->hasAccess())
	{
		echo '
		<h2>User Info</h2>
			<ul>	
				<li>'.$userArray->display_name.'</li>
				<li>'.$userArray->email.'</li>
			</ul>
		<a href="test.php">Put Test File</a>
		<form action="get.php" method="GET">
		<label>File name to get:</label>
		<input type="text" name="path"/>
		<input type="submit" />
		';
		
	}
	else
	{
		echo '
		<h2>Login</h2>
			<a href="'.$dropbox->getAccessURL().'">Login to Dropbox</a>';
	}
	?>
	
	</body>
</html>
