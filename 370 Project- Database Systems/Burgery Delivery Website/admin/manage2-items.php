<?php include('parts/menu.php'); ?>

        <!-- Main content Begins -->
        <div class="main-content">
            <div class="wrapper">
                <h1>Insert item</h1>

                <br><br>
                <form action="" method="POST" enctype="multipart/form-data">
                    <table class="tbl-30">
                        <tr>
                                <td>Name: </td>
                                <td>
                                    <input type="text" name="name" placeholder="Name of the item">
                                </td>
                        </tr>
                        <tr>
                            <td>Price: </td>
                            <td>
                                <input type="number" name="price" placeholder="Price of the item">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2">
                                <input type="submit" name="submit" value="Submit" class="button1">
                            </td>
                        </tr>

                    </table>
                </form>
            </div>
        </div>


<?php include('parts/footer.php'); ?>

<?php
    //Process value from form and save it in database
    //check whether the submit button is clicked or not

    if(isset($_POST['submit']))
    {
        //Button Clicked
        $name = $_POST['name'];
        $price = $_POST['price'];

        //SQL Query to save the data in the database
        $sql = "INSERT INTO patty SET name='$name',price='$price'";
        $conn = mysqli_connect('localhost','root','') or die(mysqli_error()); //database connection
        $db_select = mysqli_select_db($conn, 'foodie') or die(mysqli_error()); //selecting database
        $res = mysqli_query($conn, $sql) or die(mysqli_error());
        if($res==TRUE)
        {
            echo "Data Inserted";
        }
        else
        {
            echo "Failed to Insert Data";
        }
    }


?>