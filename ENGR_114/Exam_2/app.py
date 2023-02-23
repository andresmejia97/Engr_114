#app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("<p>Heyyyyyy</p>")
    return "<p>Hi</p>"

print("<p>Heyyyyyy</p>")
