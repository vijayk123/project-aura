from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Project AURA 🚀"

@app.route("/health")
def health():
      return jsonify({
        "status": "UP",
        "version": "v4"
    })
@app.route("/region")
def region():
    region = os.getenv("REGION", "unknown")
    return jsonify(region=region), 200

@app.route("/crash")
def crash():
    time.sleep(5)
    raise Exception("Simulated application crash")

# Hang endpoint (liveness probe testing)
# -------------------------
@app.route("/hang")
def hang():
    time.sleep(120)
    return "Recovered", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
