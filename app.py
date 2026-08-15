from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Dockerized Flask WebApp</h1>
    <p>Cloud Engineer Calculator API</p>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is a simple Flask web application running inside a Docker container.</p>
    <h4>Project is created by Pranav Patil for practice only </h4>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({
        "operation": "addition",
        "result": a + b
    })

@app.route("/sub/<int:a>/<int:b>")
def subtract(a, b):
    return jsonify({
        "operation": "subtraction",
        "result": a - b
    })

@app.route("/mul/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify({
        "operation": "multiplication",
        "result": a * b
    })

@app.route("/div/<int:a>/<int:b>")
def divide(a, b):

    if b == 0:
        return jsonify({
            "error": "division by zero not allowed"
        }), 400

    return jsonify({
        "operation": "division",
        "result": a / b
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)