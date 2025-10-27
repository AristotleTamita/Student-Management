from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# ---------------------
# In-memory "database"
# ---------------------
students = [
    {"id": 1, "name": "John Doe", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Jane Smith", "grade": 9, "section": "Isaiah"},
]

# ---------------------
# Common HTML Styles
# ---------------------
HTML_HEAD = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{title}</title>
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
        .container {{
            margin-top: 100px;
        }}
        .btn-custom {{
            transition: all 0.3s ease;
        }}
        .btn-custom:hover {{
            transform: scale(1.05);
        }}
        .card {{
            border-radius: 10px;
            border: none;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }}
        table th {{
            background-color: #212529;
            color: white;
        }}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="/">Flask CRUD</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a href="/" class="nav-link {home_active}">Home</a></li>
                    <li class="nav-item"><a href="/students" class="nav-link {students_active}">Students</a></li>
                    <li class="nav-item"><a href="/api/students" class="nav-link">API JSON</a></li>
                </ul>
            </div>
        </div>
    </nav>
"""

HTML_FOOTER = """
    <footer class="footer">
        <p class="mb-0">© 2025 Flask CRUD | Designed with ❤️ by You</p>
    </footer>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""

# ---------------------
# HOME PAGE
# ---------------------
@app.route('/')
def home():
    html = HTML_HEAD.format(title="Home | Flask CRUD", home_active="active", students_active="") + """
    <div class="container text-center">
        <h1 class="display-4 mb-3">Welcome to Flask CRUD!</h1>
        <p class="lead mb-4">Create, Read, Update, and Delete student records easily.</p>
        <a href="/students" class="btn btn-primary btn-lg btn-custom">Manage Students</a>
        <a href="/api/students" class="btn btn-outline-secondary btn-lg btn-custom">View JSON API</a>
    </div>
    """ + HTML_FOOTER
    return html


# ---------------------
# STUDENTS PAGE (List + Add)
# ---------------------
@app.route('/students', methods=['GET', 'POST'])
def students_page():
    global students
    message = ""

    # Create new student
    if request.method == 'POST':
        name = request.form.get('name')
        grade = request.form.get('grade')
        section = request.form.get('section')
        if name and grade and section:
            new_id = max([s['id'] for s in students], default=0) + 1
            students.append({"id": new_id, "name": name, "grade": int(grade), "section": section})
            message = f"✅ Student '{name}' added successfully!"
        else:
            message = "⚠️ Please fill in all fields."

    # Build table
    table_rows = ""
    for s in students:
        table_rows += f"""
        <tr>
            <td>{s['id']}</td>
            <td>{s['name']}</td>
            <td>{s['grade']}</td>
            <td>{s['section']}</td>
            <td>
                <a href="/students/edit/{s['id']}" class="btn btn-sm btn-warning">Edit</a>
                <a href="/students/delete/{s['id']}" class="btn btn-sm btn-danger">Delete</a>
            </td>
        </tr>
        """

    html = HTML_HEAD.format(title="Students | Flask CRUD", home_active="", students_active="active") + f"""
    <div class="container">
        <h2 class="mb-4 text-center">Student Records</h2>
        {'<div class="alert alert-info text-center">' + message + '</div>' if message else ''}
        <table class="table table-bordered table-striped">
            <thead><tr><th>ID</th><th>Name</th><th>Grade</th><th>Section</th><th>Actions</th></tr></thead>
            <tbody>{table_rows}</tbody>
        </table>
        <hr>
        <h4>Add New Student</h4>
        <form method="POST" class="row g-3">
            <div class="col-md-4"><input type="text" name="name" placeholder="Name" class="form-control" required></div>
            <div class="col-md-3"><input type="number" name="grade" placeholder="Grade" class="form-control" required></div>
            <div class="col-md-3"><input type="text" name="section" placeholder="Section" class="form-control" required></div>
            <div class="col-md-2"><button type="submit" class="btn btn-success w-100">Add</button></div>
        </form>
    </div>
    """ + HTML_FOOTER

    return html


# ---------------------
# EDIT STUDENT PAGE
# ---------------------
@app.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    global students
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return "<h3>Student not found!</h3>"

    if request.method == 'POST':
        student['name'] = request.form.get('name')
        student['grade'] = int(request.form.get('grade'))
        student['section'] = request.form.get('section')
        return redirect('/students')

    html = HTML_HEAD.format(title="Edit Student | Flask CRUD", home_active="", students_active="active") + f"""
    <div class="container">
        <div class="card mx-auto p-4" style="max-width: 500px;">
            <h3 class="text-center mb-3">Edit Student</h3>
            <form method="POST">
                <div class="mb-3">
                    <label>Name</label>
                    <input type="text" name="name" class="form-control" value="{student['name']}" required>
                </div>
                <div class="mb-3">
                    <label>Grade</label>
                    <input type="number" name="grade" class="form-control" value="{student['grade']}" required>
                </div>
                <div class="mb-3">
                    <label>Section</label>
                    <input type="text" name="section" class="form-control" value="{student['section']}" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Update</button>
                <a href="/students" class="btn btn-secondary w-100 mt-2">Cancel</a>
            </form>
        </div>
    </div>
    """ + HTML_FOOTER

    return html


# ---------------------
# DELETE STUDENT
# ---------------------
@app.route('/students/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return redirect('/students')


# ---------------------
# API ENDPOINTS (JSON)
# ---------------------
@app.route('/api/students', methods=['GET'])
def api_get_students():
    return jsonify(students)

@app.route('/api/students/<int:id>', methods=['GET'])
def api_get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    return jsonify(student or {"error": "Student not found"}), (200 if student else 404)

@app.route('/api/students', methods=['POST'])
def api_add_student():
    data = request.json
    if not data or not all(k in data for k in ('name', 'grade', 'section')):
        return jsonify({"error": "Invalid data"}), 400
    new_id = max([s['id'] for s in students], default=0) + 1
    new_student = {"id": new_id, "name": data['name'], "grade": data['grade'], "section": data['section']}
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/api/students/<int:id>', methods=['PUT'])
def api_update_student(id):
    data = request.json
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    student.update({k: data[k] for k in data if k in student})
    return jsonify(student)

@app.route('/api/students/<int:id>', methods=['DELETE'])
def api_delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({"message": f"Student {id} deleted"}), 200


# ---------------------
# Run App
# ---------------------
if __name__ == '__main__':
    app.run(debug=True)
