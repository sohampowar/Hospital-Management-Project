<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>🏥 Hospital Management System</title>
</head>
<body>

<h1>🏥 Hospital Management System</h1>

<p>A <b>Django-based web application</b> for managing hospital operations including patient registration, doctor schedules, appointments, and medical records, making hospital management efficient and organized.</p>

<hr>


<h2>📌 Project Objective</h2>
<ul>
    <li>Manage patient registrations efficiently</li>
    <li>Schedule and track doctor appointments</li>
    <li>Maintain accurate medical records</li>
    <li>Provide admins and staff with easy-to-use dashboards</li>
</ul>

<hr>

<h2>🛠️ Tools & Technologies</h2>
<ul>
    <li>Python, Django, SQLite/MySQL</li>
    <li>Frontend: HTML, CSS, Bootstrap, JavaScript</li>
    <li>Environment: VS Code, Virtual Environment</li>
    <li>Version Control: Git & GitHub</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
Hospital-Management-System/
│── manage.py           # Django management script
│── myproject/          # Project settings folder
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── apps/               # All Django apps (patients, doctors, appointments, etc.)
│── templates/          # HTML templates
│── static/             # CSS, JS, images
│── db.sqlite3          # Database file
│── requirements.txt    # Dependencies
│── README.html         # Project documentation (HTML)
│── images/             # Screenshots or visual assets
</pre>

<hr>

<h2>📊 Methodology</h2>
<ol>
    <li><b>Data Management</b>
        <ul>
            <li>Create models for Patients, Doctors, Appointments, and Medical Records</li>
            <li>Use Django ORM for CRUD operations</li>
            <li>Handle validations and relationships between models</li>
        </ul>
    </li>
    <li><b>Views & Templates</b>
        <ul>
            <li>Create views for listing, adding, editing, and deleting records</li>
            <li>Use Django templates for rendering UI</li>
            <li>Integrate Bootstrap for responsive design</li>
        </ul>
    </li>
    <li><b>User Interaction</b>
        <ul>
            <li>Implement forms for patient registration and appointment booking</li>
            <li>Dashboard for admin and staff</li>
            <li>Search and filter functionalities</li>
        </ul>
    </li>
</ol>

<hr>

<h2>📌 Features</h2>
<ul>
    <li>Patient registration and management</li>
    <li>Doctor scheduling and appointment booking</li>
    <li>Medical records management</li>
    <li>Admin and staff dashboards</li>
    <li>Search, edit, and delete functionalities</li>
</ul>

<hr>

<h2>🚀 How to Run Locally</h2>
<ol>
    <li>Clone the repository
        <pre>git clone https://github.com/your-username/Hospital-Management-System.git</pre>
    </li>
    <li>Navigate to the project folder
        <pre>cd Hospital-Management-System</pre>
    </li>
    <li>Create a virtual environment
        <pre>python -m venv venv</pre>
    </li>
    <li>Activate the virtual environment
        <pre>
<!-- Windows -->
venv\Scripts\activate

<!-- Linux / Mac -->
source venv/bin/activate
        </pre>
    </li>
    <li>Install dependencies
        <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Apply migrations and run the server
        <pre>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
        </pre>
    </li>
</ol>

<hr>

<h2>🙋‍♂️ Author</h2>
<p>
<b>Your Name</b><br>
B.Tech in Computer Science & Engineering<br>
GitHub: <a href="https://github.com/sohampowar">SohampowarGithub</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/soham-powar-383593271/">SohampowarLinkedIn</a>
</p>

</body>
</html>
