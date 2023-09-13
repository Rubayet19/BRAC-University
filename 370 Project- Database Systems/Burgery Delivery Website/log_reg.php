<?php 

require('connection.php');
session_start();


#for admin login
if(isset($_POST['adminlogin']))
{
  $query="SELECT * FROM `admin` WHERE `email`='$_POST[email]' and `password`='$_POST[password]'";
  $result=mysqli_query($con,$query);
  
  if($result)
  {
    if(mysqli_num_rows($result)==1)
    {
      $result_fetch=mysqli_fetch_assoc($result);
     
      
       $_SESSION['logged_in']=true;
        $_SESSION['email']=$result_fetch['email'];
        header("location: admin/index.php");
    }
      else
      {
        echo"
          <script>
            alert('Incorrect Password or Wrong email');
            window.location.href='index.php';
          </script>
        ";
      }
    }
  
}
   



#for login
if(isset($_POST['login']))
{
  $query="SELECT * FROM `user_reg` WHERE `Email`='$_POST[email]'";
  $result=mysqli_query($con,$query);
  
  if($result)
  {
    if(mysqli_num_rows($result)==1)
    {
     
      $result_fetch=mysqli_fetch_assoc($result);
      if(password_verify($_POST['password'],$result_fetch['password']))
      {
        $_SESSION['logged_in']=true;
        $_SESSION['email']=$result_fetch['Email'];
        header("location: index.php");

      }
      else{
        echo"
        <script>
          alert('wrong password');
          window.location.href='index.php';
        </script>
      ";
}
    }
    else
    {
      echo"
        <script>
          alert('Email not registered or wrong password');
          window.location.href='index.php';
        </script>
      ";
    }
  }
  else
  {
    echo"
      <script>
        alert('Cannot Run Query');
        window.location.href='index.php';
      </script>
    ";
  }
}







#for registration
if(isset($_POST['register']))
{
  $user_exist_query="SELECT * FROM `user_reg` WHERE `Email`='$_POST[email]'";
  $result=mysqli_query($con,$user_exist_query);

  if($result)
  {

    if(mysqli_num_rows($result)>0) #it will be executed if email is already taken
    {
      $result_fetch=mysqli_fetch_assoc($result);
      if($result_fetch['Email']==$_POST['email'])
      {
        #error for email already registered
        echo"
          <script>
            alert('$result_fetch[Email] - email already taken');
            window.location.href = 'index.php';
        </script>
        ";
      }
      else{

      }
    }
    else #it will be executed if the email is new
    {
      
      $password=password_hash($_POST['password'],PASSWORD_BCRYPT);
        $query="INSERT INTO `user_reg`(`name`, `password`, `Email`) VALUES ('$_POST[fullname]','$password','$_POST[email]')";
        if(mysqli_query($con,$query))
        {
           # It will be executed if data is inserted correctly
           echo"
            <script>
              alert('Registration successful');
              window.location.href = 'index.php';
          </script>
          ";
        }
        else   # It will be executed if data is not inserted correctly
        {
            echo"
            <script>
              alert('Error Occured');
              window.location.href = 'index.php';
          </script>
          ";
        }
    }
  }
  else
  {
    echo"
      <script>
        alert('Error Run Query');
        window.location.href='index.php';
      </script>
    ";
  }
}

?>