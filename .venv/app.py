from flask import Flask
app = Flask (__name__)
@app.route("/")
def home():
    return"Hi team, this is my python project for the web application created by Pragadesh"