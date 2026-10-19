from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from AWS EC2!"

@app.route("/health")
def health():
    return "Application is healthy"

@app.route("/version")
def version():
    return "Version 1.0"

app.run(host="0.0.0.0", port=5000)
