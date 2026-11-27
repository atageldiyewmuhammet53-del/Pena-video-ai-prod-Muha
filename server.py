from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name": "PENA VIDEO AI PRO",
        "status": "Server online",
        "ai_connected": False
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
