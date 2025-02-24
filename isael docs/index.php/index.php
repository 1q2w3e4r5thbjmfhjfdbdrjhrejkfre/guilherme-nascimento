<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Calculando a sua idade</h1>

    <form method="POST">
        <input type="password" name="age">
        <button type="submit">Calcular</button>
    </form>

    <?php
    //verificando se a variável existe ou é diferente
    if(!isset($_REQUEST['age'])){
        return null;
    }else{
      $idade = 2025 - $_REQUEST['age'];
      echo "$idade anos";
    }
?>
</body>
</html>