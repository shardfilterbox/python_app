from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "My name is Shard Vicens, and this is my first Python script, using CircleCI for contant integration."