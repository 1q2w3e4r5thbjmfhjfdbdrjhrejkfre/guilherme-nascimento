<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estacionamento</title>
    <style>
        .container {
            display: flex;
            flex-direction: row;
        }
        .container div {
            background-color: #ccc;
            width: 50%;
            height: 150px;
            border: 1px solid #000;
            border-radius: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <form method="post">
        <input type="text" name="placa">
        <input type="time" name="hora_ent">
        <button type="submit">Registar entrada</button>
        </form>
    </div>
    <div class="container">
        <form method="post"></form>
        <input type="text" name="placa">
        <input type="time" name="hora_ent">
        <button type="submit">Registar entrada</button>
    </div>
    </form>
<?php
$nome = "edson";
$file = fopen('arquivo.txt', 'a');
fwrite($file, "edson");
//fwritte($file, "edson");

fclose($file);

?>  
</body>
</html>   
