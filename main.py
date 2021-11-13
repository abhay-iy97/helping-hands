from flask import Flask, redirect, url_for, render_template, request

#initalizing flask app
app = Flask(__name__)
app.secret_key = 'my secret and not your secret'


# @app.route('/aboutus')
# def about():
#     return render_template("about.html")


@app.route('/')
def index():
    return render_template("index.html")