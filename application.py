#! /usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template(
        "home.html")

@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    todo=["rien", "pas grand chose", "sieste"]
    return render_template(
        "user.html",
        name=name,
        todo=todo)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
