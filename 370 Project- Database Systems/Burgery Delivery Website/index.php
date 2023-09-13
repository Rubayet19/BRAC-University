<?php 
  require('connection.php'); 
  session_start();
  $placedorder=0;
 if(isset($_GET['msg']) && $_GET['msg'] == 'success')
 {
     $placedorder=1;
    unset($_SESSION["shopping_cart"]);
 }


  if(isset($_POST["add_to_cart"]))
{
 if(isset($_SESSION["shopping_cart"]))
 {
 $item_array_id = array_column($_SESSION["shopping_cart"], "item_id");
 if(!in_array($_GET["id"], $item_array_id))
 {
 $count = count($_SESSION["shopping_cart"]);
 $item_array = array(
 'item_id' => $_GET["id"],
 'item_name' => $_POST["hidden_name"],
 'item_price' => $_POST["hidden_price"],
 'item_quantity' => $_POST["quantity"]
 );
 $_SESSION["shopping_cart"][$count] = $item_array;
 }

 }
 else
 {
 $item_array = array(
 'item_id' => $_GET["id"],
 'item_name' => $_POST["hidden_name"],
 'item_price' => $_POST["hidden_price"],
 'item_quantity' => $_POST["quantity"]
 );
 $_SESSION["shopping_cart"][0] = $item_array;
 }
}
 
if(isset($_GET["action"]))
{
 if($_GET["action"] == "delete")
 {
 foreach($_SESSION["shopping_cart"] as $keys => $values)
 {
 if($values["item_id"] == $_GET["id"])
 {
 unset($_SESSION["shopping_cart"][$keys]);
 echo '<script>alert("Item Removed")</script>';
 echo '<script>window.location="index.php"</script>';
 }
 }
 }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User/Admin Login and Register</title>
    <link rel="stylesheet" href="bootstrap-5.0.2-dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/mainpage.css">

    <link rel="stylesheet" href="ami.css">
    <link rel="stylesheet" href="ji.css">
    <style>
    body {
  background-color: lightblue;
}
</style>
<ul class="nav">
        <li><a href="index.php">Home</a></li>
        <li><a href="#">Food Menu</a></li>
        <?php
        if($placedorder==1)
        {
            ?>
        <li><a href="#"onclick="statusfunction()">View Status</a></li> 
        <?php    
    }
        
        ?>
    </ul>
    <hr style="height:6px; background-color:yellow">
</head>


<body>
    <img class="bg" src="burger1.jpg" alt="">
    <header>

        <div class="head">
        
            <h2>Katsuma Burger Delivery</h2>
        </div>


        <div class="sign-in-up">
            <button type="button" onclick="popup('User login')">User-login</button>
            <button type="button" onclick="popup('User registration')">User-Registration</button>
            <button type="button" onclick="popup('Admin login')">Admin-login</button>
        </div>
    </header>
    <div class="container" id="User login">
        <div class="pop">
            <form method="POST" action="log_reg.php">
                <h2>
                    <span>User login</span>
                    <button type="reset">Reset</button>
                    <button type="reset" class=mybtn onclick="popup('User login')">X</button>
                </h2>
                <input type="email" placeholder="E-mail" name="email">
                <input type="password" placeholder="Password" name="password">
                <button type="submit" class="login-btn" name="login">Login</button>
            </form>
        </div>
    </div>



    <div class="container" id="User registration">
        <div class="reg-pop">
            <form method="POST" action="log_reg.php">
                <h2>
                    <span>User Registration</span>
                    <button type="reset">Reset</button>
                    <button type="reset" class=mybtn onclick="popup('User registration')">X</button>
                </h2>
                <input type="text" placeholder="Full Name" name="fullname">
                <input type="email" placeholder="E-mail" name="email">
                <input type="password" placeholder="Password" name="password">
                <button type="submit" class="reg-btn" name="register">Complete Registration</button>
            </form>
        </div>
    </div>

    <div class="container" id="Admin login">
        <div class="ad-pop">
            <form method="POST" action="log_reg.php">
                <h2>
                    <span>Admin Login</span>
                    <button type="reset">Reset</button>
                    <button type="reset" class=mybtn onclick="popup('Admin login')">X</button>
                </h2>
                <input type="email" placeholder="E-mail" name="email">
                <input type="password" placeholder="Password" name="password">
                <button type="submit" class="ad-btn" name="adminlogin">Login</button>
            </form>
        </div>
    </div>
    
    <div class="row">
    <H3>Burgers</H3>
    <?php
      $selectquery="select * from burger";
     $query=mysqli_query($con,$selectquery);
      $nums=mysqli_num_rows($query);
     while ( $nax=mysqli_fetch_array($query)){
        ?>
            <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">
 

<h4 class="text-info"><?php echo $nax["name"]; ?></h4>
 
 <h4 class="text-danger"><?php echo $nax["burger_price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["name"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["burger_price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] ==  true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>
                        
 </div>
 </form>
                    </div>
                    <?php

}
?>
</div>
<div class="row">
<H3>BUN</H3>

<?php
      $selectquery="select * from bun";
      $query=mysqli_query($con,$selectquery);
       $nums=mysqli_num_rows($query);
      while ( $nax=mysqli_fetch_array($query)){
        ?>
 <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">

<h4 class="text-info"><?php echo $nax["name"]; ?></h4>
 
 <h4 class="text-danger"><?php echo $nax["price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["name"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] == true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>                    
 </div>
 </form>
                    </div>
                    <?php

                        }
                        ?>
                        </div>
        <div class="row">
        <H3>PATTY</H3>
        <?php
      $selectquery="select * from patty";
      $query=mysqli_query($con,$selectquery);
       $nums=mysqli_num_rows($query);
      while ( $nax=mysqli_fetch_array($query)){
        ?>
                    <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">

<h4 class="text-info"><?php echo $nax["name"]; ?></h4>
 
 <h4 class="text-danger"><?php echo $nax["price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["name"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] == true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>
                       
 </div>
 </form>
                    </div>
                    <?php

}
?>
</div>
<div class="row">
<H3>SALAD</H3>
<?php
$selectquery="select * from salad";
$query=mysqli_query($con,$selectquery);
 $nums=mysqli_num_rows($query);
while ( $nax=mysqli_fetch_array($query)){
        ?>
                    <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">
 

 

<h4 class="text-info"><?php echo $nax["name"]; ?></h4>
 
 <h4 class="text-danger"> <?php echo $nax["price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["name"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] == true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>
                        
 </div>
 </form>
                    </div>
                    <?php

                        }
                        ?>
                        </div>
<div class="row">
 <H3>SAUCE</H3>
 <?php
 $selectquery="select * from sauce";
 $query=mysqli_query($con,$selectquery);
  $nums=mysqli_num_rows($query);
 while ( $nax=mysqli_fetch_array($query)){
        ?>
                    <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">

 

<h4 class="text-info"><?php echo $nax["name"]; ?></h4>
 
 <h4 class="text-danger"> <?php echo $nax["price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["name"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] == true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>
                        
 </div>
 </form>
                    </div>
                    <?php

                        }
                        ?>
                        </div>
                        <div class="row">
                        <H3>SPICE LEVEL</H3>
                        <?php
 $selectquery="select * from spice_level";
 $query=mysqli_query($con,$selectquery);
  $nums=mysqli_num_rows($query);
 while ( $nax=mysqli_fetch_array($query)){
        ?>
                    <div class="col-md-4" >
 <form method="post" action="index.php?action=add&id=<?php echo $nax["id"]; ?>">
 <div style="border:3px solid #5cb85c; background-color:whitesmoke; border-radius:5px; padding:16px; margin:8px;" align="center">
<h4 class="text-info"><?php echo $nax["level"]; ?></h4>
 
 <h4 class="text-danger"> <?php echo $nax["price"]; ?> tk</h4>
 
 <input type="text" name="quantity" value="1" class="form-control" />
 
 <input type="hidden" name="hidden_name" value="<?php echo $nax["level"]; ?>" />
 
 <input type="hidden" name="hidden_price" value="<?php echo $nax["price"]; ?>" />
 <?php
 if(@$_SESSION['logged_in'] == true)
 {
 ?>
 <input type="submit" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
<?php
}
else
{
    ?>
    <input type="button" onclick="notLogin()" name="add_to_cart" style="margin-top:5px;" class="btn btn-success" value="Add to Cart" />
   <?php

}
?>
 </div>
 </form>
                    </div>
                    <?php

}
?>
                    </div>


                    <div style="clear:both"></div>
 <br />
 <h3>Order Details</h3>
 <div class="table-responsive">
 <table class="table table-bordered">
 <tr>
 <th width="40%">Item Name</th>
 <th width="10%">Quantity</th>
 <th width="20%">Price</th>
 <th width="15%">Total</th>
 <th width="5%">Action</th>
 </tr>
 <?php
 if(!empty($_SESSION["shopping_cart"]))
 {
 $total = 0;
 foreach($_SESSION["shopping_cart"] as $keys => $values)
 {
 ?>
 <tr>
 <td><?php echo $values["item_name"]; ?></td>
 <td><?php echo $values["item_quantity"]; ?></td>
 <td>$ <?php echo $values["item_price"]; ?></td>
 <td>$ <?php echo number_format($values["item_quantity"] * $values["item_price"], 2);?></td>
 <td><a href="index.php?action=delete&id=<?php echo $values["item_id"]; ?>"><span class="text-danger">Remove</span></a></td>

</tr>
 <?php
 $total = $total + ($values["item_quantity"] * $values["item_price"]);
 }
 ?>
 <tr>
 <td colspan="3" align="right">Total</td>
 <td align="right">$ <?php echo number_format($total, 2); ?></td>
 <td> <button onclick="myFunction()">Place Order</button></td>
 </tr>
 <?php
 }
 ?>
 
 </table>
 </div>
 </div>
 </div>


    <script>
        function popup(popup_name) {
            get_popup = document.getElementById(popup_name);
            if (get_popup.style.display == "flex") {

                get_popup.style.display = "none";
            }
            else {
                get_popup.style.display = "flex";
            }
        }
        function myFunction() {
  alert("Your order has been Confirmed!");
  window.location.href = "index.php?msg=success";
        }
        function statusfunction() {
  alert("Your order is on the way!");
  window.location.href = "index.php";
        }
function notLogin() {
  alert("Please login first to create an order!");
  //window.location.href = "index.php";
        }
    </script>


</body>
<footer>
  <p class="text-center">2021 All Rights Reserved,<a>Katsuma Burger Delivery</a> Developed By: Group 7</p>
</footer>
</html>