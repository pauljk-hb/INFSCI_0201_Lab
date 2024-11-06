from flask import Flask, render_template, request, redirect, url_for, flash
from nasa_apod import fetch_apod
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    try:
        apod_data = fetch_apod()
    except Exception as e:
        apod_data = None
        flash("Fehler beim Abrufen des APOD-Bildes.")
    return render_template("index.html", apod_data=apod_data)

@app.route("/history", methods=["GET", "POST"])
def history():
    apod_data = None
    selected_date = None
    
    if request.method == "POST":
        selected_date = request.form.get("date")
        
        if selected_date:
            apod_data = fetch_apod(selected_date)
    
    return render_template("history.html", current_date=datetime.now().strftime('%Y-%m-%d'), apod_data=apod_data, selected_date=selected_date)

