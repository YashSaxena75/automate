<html>

<head>
  <meta charset="UTF-8">
  <title>Navigation Bar</title>
 <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300">
      <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="menu-nav">
  <div id="navigation-bar">
    <ul>
      <li><a href="form.php"><i class="fa fa-home"></i><span>Home</span></a></li>
      <li><a href="#"><i class="fa fa-handshake"></i><span>Services</span></a></li>
      <li><a href="#"><i class="fa fa-user"></i><span>About</span></a></li>
      <li><a href="form1.php"><i class="fa fa-book"></i><span>Contact</span></a></li>
    </ul>
  </div>

  </div>
<br><br>
</body>
</html>

<?php
if(isset($_POST["sub"]))
{
$price=$_POST['ptag'];
if ($price==100)
{
echo $price;
}
else
{
echo "done!";
}
}
?>
