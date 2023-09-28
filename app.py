from flask import Flask, render_template, request
from jinja2 import Template
import datetime
import json

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():

        try:
            with open('./data/data.json', 'r') as file:
                    data = json.load(file)
        except FileNotFoundError:
            data = {"entries": []}

        if request.method == "POST":
            entry_content = request.form.get("content")
            current_date = datetime.datetime.today().strftime("%d-%m-%Y")
            current_time = datetime.datetime.now().strftime("%H:%M")

            # Read the existing JSON file
            with open('./data/data.json', 'r') as file:
                data = json.load(file)

            # Append the new entry to the data structure
            data["entries"].append({
                "text": entry_content,
                "date": current_date,
                "time": current_time
            })

            # Write the updated data structure back to the JSON file
            with open('./data/data.json', 'w') as file:
                json.dump(data, file)

        return render_template("home.html", entries=data["entries"])
    
    return app
