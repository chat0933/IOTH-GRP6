from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from alarm_db import create_user_table_chris, create_issues_table_chris
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)

app.secret_key = "abemadXD"
app.permanent_session_lifetime = timedelta(minutes=5)

###Routes
#the main socketio that emites to the webpage
@socketio.on('patient_database')
def PatientData():
    value0 = 'PATIENT_ID' 
    value1 = 'FALLEN'
    value2 = 'HEARTH_RATE'
    value3 = 'GPS1'
    value4 = 'GPS2'
    Data = [value0, value1, value2, value3, value4]
    socketio.emit('PD', Data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/register", methods= ["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        create_user_table_chris() 
        conn = sqlite3.connect("patient_database.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (USERNAME, PASSWORD) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        flash(f"Registration successful, {username}! Please log in.")
        return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/login", methods= ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        entered_username = request.form["username"]
        entered_password = request.form["password"]

        conn = sqlite3.connect("patient_database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE USERNAME=?", (entered_username,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user[1], entered_password):
            # user[2] is the hashed password stored in the database
            session["user"] = entered_username
            flash(f"Welcome to Rynkeby, Mr. {entered_username}")
            return redirect(url_for("user"))
        else:
            flash("Invalid username or password. Please try again.", "error")
            return redirect(url_for("login"))
    else:
        if "user" in session:
            flash(f"You are already logged in, {session['user']}! Are you old or what?")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Hej! Hvem er du?")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("Tak for denne gang, vi savner dig allerede", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/dashboard")
def update_dashboard():
    
    create_issues_table_chris()  # Make sure your table is created before querying it
    conn = sqlite3.connect("patient_database.db")
    cur = conn.cursor()
    
    # Execute the SQL query
    cur.execute("SELECT * FROM Issues ORDER BY PATIENT_ID DESC LIMIT 30")
    
    # Fetch all rows
    patient_data = cur.fetchall()
    
    # Close the cursor and connection when done
    cur.close()
    conn.close()
    
    # Render the template with the fetched data
    return render_template("dashboard.html", patient_data=patient_data)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)