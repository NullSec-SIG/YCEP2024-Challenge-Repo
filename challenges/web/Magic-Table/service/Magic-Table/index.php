<!-- Credit to: https://medium.com/aratta-studios/three-js-tutorial-how-to-make-a-periodic-table-99be4c772117 -->

<!DOCTYPE html>
<html>

<head>
    <title>Magic Table</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    <style>
        html,
        body {
            height: 100%;
        }

        body {
            background-color: #000000;
            margin: 0;
            font-family: Helvetica, sans-serif;
            ;
            overflow: hidden;
        }

        a {
            color: #ffffff;
        }

        #menu {
            position: absolute;
            bottom: 20px;
            width: 100%;
            text-align: center;
        }

        .element {
            width: 120px;
            height: 160px;
            box-shadow: 0px 0px 12px rgba(0, 255, 255, 0.5);
            border: 1px solid rgba(127, 255, 255, 0.25);
            text-align: center;
            cursor: default;
        }

        .element:hover {
            box-shadow: 0px 0px 12px rgba(0, 255, 255, 0.75);
            border: 1px solid rgba(127, 255, 255, 0.75);
        }

        .element .number {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 12px;
            color: rgba(127, 255, 255, 0.75);
        }

        .symbol {
            text-align: center;
            position: absolute;
            top: 40px;
            left: 0px;
            right: 0px;
            font-size: 60px;
            font-weight: bold;
            color: rgba(255, 255, 255, 0.75);
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.95);
        }

        .element .details {
            position: absolute;
            bottom: 15px;
            left: 0px;
            right: 0px;
            font-size: 12px;
            color: rgba(127, 255, 255, 0.75);
        }

        button {
            color: rgba(127, 255, 255, 0.75);
            background: transparent;
            outline: 1px solid rgba(127, 255, 255, 0.75);
            border: 0px;
            padding: 5px 10px;
            cursor: pointer;
        }

        button:hover {
            background-color: rgba(0, 255, 255, 0.5);
        }

        button:active {
            color: #000000;
            background-color: rgba(0, 255, 255, 0.75);
        }
    </style>
</head>

<body>
    <script src="res/three.js"></script>
    <script src="res/Tween.min.js"></script>
    <script src="res/TrackballControls.js"></script>
    <script src="res/CSS3DRenderer.js"></script>

    <h1 id="status" class="symbol" style="margin-top: 0px; margin-bottom: 20px;">Not enough elements selected</h1>

    <div id="container"></div>

    <script src="main.js"></script>
</body>

</html>