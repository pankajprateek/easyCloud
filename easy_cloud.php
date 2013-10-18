<?php

class Easycloud{

// return html for the folder structure given the array
	function getHTML($arr) {
	    $nl = "<br>\n";
	    
	    $s = "	    
	    <table class = 'table table-striped table-bordered table-condensed'> 
		<thead> <tr> <td> Files/Folders </td> <td> Stored at </td> <td> Last modified </td> </tr></thead>
		<tbody> 
	    ";
			    	    
	    foreach($arr as $a) {
		//var_dump($a);
		//$s .=  $nl;
		if($a['is_dir'] == 1) {
		  $s .= "<tr> <td> <a href = ''>". $a['path'] ."</a> </td> <td>". $a['stored_at'] ."</td> <td>". $a['last_modified'] ."</td> </tr>";
		} else { 
		  $s .= "<tr> <td>". $a['path'] ."</td> <td>". $a['stored_at'] ."</td> <td>". $a['last_modified'] ."</td> </tr>";
		}			
	    }	
	    
	    $s .= "</tbody>
	    </table>
	    ";
	    return $s;
	}
}
?>