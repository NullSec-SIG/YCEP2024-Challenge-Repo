from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

trips = [
    {"route": "Seoul to Busan", "time": "08:00 AM"},
    {"route": "Seoul to Busan", "time": "12:00 PM"},
    {"route": "Seoul to Busan", "time": "04:00 PM"},
    {"route": "Seoul to Busan", "time": "08:00 PM"},
    {"route": "Seoul to Daejeon", "time": "10:00 AM"},
    {"route": "Seoul to Daejeon", "time": "02:00 PM"}
]

BLACKLISTED_STRINGS = ['\'', '\"', '[', ']', 'os', 'subprocess']

CONFIRMATION_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>KTX - Confirmation Page</title>
</head>
<body>
    <header>
        <a href="/">
            <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo" class="logo">
        </a>
        <nav>
            <button>Info</button>
            <button>Tickets</button>
            <button>Pass</button>
        </nav>
    </header>

    <main>
        <img src="{{ url_for('static', filename='banner.jpeg') }}" alt="Placeholder Image" class="placeholder-image">
        <div class="form-container">
            <h1>Ticket Confirmation</h1>
            {% if not blacklisted %}
                <p>Your ticket for <strong>TRIP</strong> has been confirmed.</p>
            {% else %}
                <p>Your reservation was unsuccessful!</p>
            {% endif %}

            <h2>Train Timings</h2>
            <table>
                <thead>
                    <tr>
                        <th>Route</th>
                        <th>Time</th>
                    </tr>
                </thead>
                <tbody>
                    {% for trip in trips %}
                        <tr>
                            <td>{{ trip['route'] }}</td>
                            <td>{{ trip['time'] }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template('index.html', trips=trips)


@app.route('/confirmation')
def confirmation():
    trip = request.args.get('trip')
    blacklisted = any([w in trip.lower() for w in BLACKLISTED_STRINGS])

    return render_template_string(
        CONFIRMATION_TEMPLATE.replace("TRIP", trip),
        trips=trips,
        blacklisted=blacklisted
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0")
