<?php include('parts/menu.php'); ?>

        <!-- Main content Begins -->
        <div class="main-content">
            <div class="wrapper">
                <h1>Delete item</h1>

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
                            <td colspan="2">
                                <input type="submit" name="submit" value="Delete" class="button1">
                            </td>
                        </tr>

                    </table>
                </form>
            </div>
        </div>


<?php include('parts/footer.php'); ?>

<?php
    //Process value from form and delete it from database
    //check whether the submit button is clicked or not

    if(isset($_POST['submit']))
    {
        //Button Clicked
        $name = $_POST['name'];

        //SQL Query to delete the data in the database
        $conn = mysqli_connect('localhost','root','') or die(mysqli_error()); //database connection
        $db_select = mysqli_select_db($conn, 'foodie') or die(mysqli_error()); //selecting database
        $sql = "DELETE FROM salad WHERE name='$name'";
        $res = mysqli_query($conn, $sql) or die(mysqli_error());
        if($res==TRUE)
        {
            echo "Data Deleted";
        }
        else
        {
            echo "Failed to Delete Data";
        }
    }


?>