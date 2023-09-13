<?php

  $con=mysqli_connect("localhost","root","","foodie");

  if(mysqli_connect_error()){
    echo"<script>alert('cannot connect to the database');</script>";
    exit();
  }

?>