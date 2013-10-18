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
			$nl = "<br>\n";
			$arr = $dropbox->getFolder('root', NULL);
			echo $nl.$nl;
			echo $dropbox->getHTML($arr);	     
			
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
