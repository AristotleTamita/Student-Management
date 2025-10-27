from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------------------
# HOME PAGE (Styled)
# ---------------------
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Home | Flask API</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
        <style>
            body {
                background-color: #f4f7fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .navbar-brand {
                font-weight: bold;
                font-size: 1.3rem;
            }
            .footer {
                position: fixed;
                width: 100%;
                bottom: 0;
                background-color: #212529;
                color: white;
                text-align: center;
                padding: 10px 0;
            }
            .hero {
                margin-top: 120px;
            }
            .btn-custom {
                margin: 5px;
                transition: all 0.3s ease;
            }
            .btn-custom:hover {
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <div class="container">
                <a class="navbar-brand" href="/">Flask API</a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a href="/" class="nav-link active">Home</a></li>
                        <li class="nav-item"><a href="/student" class="nav-link">Student</a></li>
                        <li class="nav-item"><a href="/api/student" class="nav-link">API JSON</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container text-center hero">
            <h1 class="display-4 mb-3">Welcome to My Flask API!</h1>
            <p class="lead mb-4">A clean and modern Flask web app with built-in design.</p>
            <a href="/student" class="btn btn-primary btn-lg btn-custom">View Student Info</a>
            <a href="/api/student" class="btn btn-outline-secondary btn-lg btn-custom">View JSON API</a>
        </div>

        <footer class="footer">
            <p class="mb-0">© 2025 Flask API | Designed with ❤️ by You</p>
        </footer>

        <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js'></script>
    </body>
    </html>
    """

# ---------------------
# STUDENT PAGE (Styled)
# ---------------------
@app.route('/student')
def student_page():
    student_data = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }

    return f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Student Info | Flask API</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
        <style>
            body {{
                background-color: #f4f7fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .navbar-brand {{
                font-weight: bold;
                font-size: 1.3rem;
            }}
            .footer {{
                position: fixed;
                width: 100%;
                bottom: 0;
                background-color: #212529;
                color: white;
                text-align: center;
                padding: 10px 0;
            }}
            .card {{
                margin-top: 100px;
                border: none;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}
            .btn-custom {{
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <div class="container">
                <a class="navbar-brand" href="/">Flask API</a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
                        <li class="nav-item"><a href="/student" class="nav-link active">Student</a></li>
                        <li class="nav-item"><a href="/api/student" class="nav-link">API JSON</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="card mx-auto text-center p-4" style="max-width: 500px;">
                <h3 class="mb-3">Student Information</h3>
                <p><strong>Name:</strong> {student_data['name']}</p>
                <p><strong>Grade:</strong> {student_data['grade']}</p>
                <p><strong>Section:</strong> {student_data['section']}</p>
                <a href="/" class="btn btn-secondary btn-custom">Back Home</a>
            </div>
        </div>

        <footer class="footer">
            <p class="mb-0">© 2025 Flask API | Designed with ❤️ by You</p>
        </footer>

        <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js'></script>
    </body>
    </html>
    """

# ---------------------
# STUDENT API (JSON)
# ---------------------
@app.route('/api/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# ---------------------
# Run App
# ---------------------
if __name__ == '__main__':
    app.run(debug=True)
