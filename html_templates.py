from string import Template

index_template = Template('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            margin: 0;
            padding: 0;
        }
        h1 {
            text-align: center;
            margin-top: 50px;
            font-size: 36px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        #bird-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .bird-card {
            background: linear-gradient(45deg, #ff4e50, #ff9f4d);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px;
            padding: 20px;
            width: 300px;
            text-align: center;
            transition: transform 0.3s ease-in-out;
        }
        .bird-card:hover {
            transform: translateY(-5px);
        }
        .bird-card img {
            max-width: 100%;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .bird-card h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .bird-card h3 {
            font-size: 18px;
            color: #fff;
        }
    </style>
</head>
<body>
    <h1>Aves de Chile</h1>
    <div id="bird-list">
        $bird_cards
    </div>
</body>
</html>''')

bird_card_template = Template('''<div class="bird-card">
    <img src="$image" alt="$nombre_espanol">
    <h2>$nombre_espanol</h2>
    <h3>$nombre_ingles</h3>
</div>''')
