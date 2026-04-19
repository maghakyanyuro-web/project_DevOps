from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Hello from Kubernetes!</h1><p>Running on: {os.uname()[1]}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
