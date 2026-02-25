from flask import Flask, request, jsonify
from flask_cors import CORS
from services.log_service import process_log

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    log = data.get("log")

    result = process_log(log)

    return jsonify(result)
from flask import render_template

@app.route("/")
def dashboard():
    return render_template("dashboard.html")