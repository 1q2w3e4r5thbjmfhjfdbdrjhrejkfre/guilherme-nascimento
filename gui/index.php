<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Temperatura</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }

        h1 {
            color:rgb(255, 39, 1);
            font-size: 2.5em;
            margin-bottom: 20px;
        }

        form {
            background-color:rgb(32, 255, 44);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 300px;
        }

        input[type="text"], select {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 2px solidrgb(255, 0, 0);
            font-size: 1.1em;
        }

        button {
            background-color:rgb(255, 234, 1);
            color: white;
            padding: 12px;
            font-size: 1.2em;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color:rgb(1, 141, 255);
        }

        p {
            color:rgb(255, 1, 170);
            font-size: 1.3em;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Calculadora de Gaby</h1>

    <form method="GET">
        <input type="text" name="temperatura" placeholder="Digite a temperatura" required>
        <select name="conversão" required>
            <option value="opcao">Escolha uma opção</option>
            <option value="fc">Fahrenheit para Celsius</option>
            <option value="cf">Celsius para Fahrenheit</option>
            <option value="ck">Celsius para Kelvin</option>
            <option value="kc">Kelvin para Celsius</option>
        </select>
        <button type="submit">Converter</button>
    </form>

    <?php
    if (isset($_GET['temperatura']) && isset($_GET['conversão'])) {
        $temperatura = $_GET['temperatura'];
        $conversao = $_GET['conversão'];

        if (is_numeric($temperatura)) {
            switch ($conversao) {
                case 'fc':
                    $resultado = ($temperatura - 32) * 5/9;
                    echo "<p>$temperatura °F é igual a $resultado °C</p>";
                    break;
                case 'cf':
                    $resultado = ($temperatura * 9/5) + 32;
                    echo "<p>$temperatura °C é igual a $resultado °F</p>";
                    break;
                case 'ck':
                    $resultado = $temperatura + 273.15;
                    echo "<p>$temperatura °C é igual a $resultado K</p>";
                    break;
                case 'kc':
                    $resultado = $temperatura - 273.15;
                    echo "<p>$temperatura K é igual a $resultado °C</p>";
                    break;
                default:
                    echo "<p>Por favor, escolha uma opção válida de conversão.</p>";
            }
        } else {
            echo "<p>Por favor, insira um valor numérico válido para a temperatura.</p>";
        }
    }
    ?>

</body>
</html>
