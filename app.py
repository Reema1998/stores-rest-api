from flask import Flask

app = Flask(__name__)

# it creates an endpoint
@app.route('/')  


def home():
    return "Hello World!!"

app.run(port=3000)