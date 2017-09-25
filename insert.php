<?php
    //------insert.php------

    // Create connection
    $conn = new mysqli(localhost,sajjan72,,folium);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 


          $data=$_POST['convertedData'];
          
          $sql= mysqli_query($conn,"INSERT INTO drawData(data) VALUES('".$data."')");
?>