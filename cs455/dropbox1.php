<?php
var_dump($_POST);
//var_dump(getallheaders());
echo "./";
var_dump ($_SERVER['PATH_INFO']);

?>

<html>
<head>
<script type = "text/javascript">
   if(window.location.hash) {
         var screen = window.location.hash.substring(1); //Puts hash in variable, and removes the # character         
         ajax.getRequest("dropbox2.php",["screen"], [screen],function(data){
            alert(data);
         });                  
         // hash found
     } else {
         // No hash found
     }
</script>
</head>
</html>