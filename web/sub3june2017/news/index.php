<?php
  session_start();
  if(array_key_exists('user', $_SESSION)) {
    // check type of user then
    header("Location: add.php");
    header("Location: view.php");
  }
?>
<!DOCTYPE html>
<head>
  <?php
  ?>
</head>
<body>
  <div id="header">
    Welcome to news, please login
  </div>
  <?php
    if(array_key_exists('user', $_SESSION)) { ?>
      <p>
        Logged in as <?php echo $_SESSION['user']?>
      </p>
      <form action="./forms/logout.php" method="post">
        <input type="submit" value="Logout" />
      </form>
    <?php } else { ?>
      <form action="./forms/login.php" method="post">
        <label>user</label>
        <input name="user" type="text" />
        <br />
        <label>password</label>
        <input name="password" type="password" />
        <br />
        <input type="submit" value="Login" />
      </form>
  <?php } ?>
</body>
