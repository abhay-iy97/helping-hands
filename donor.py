from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donorAccess', methods=['POST', 'GET'])
def login():
    username = request.args.get('email')
    password = request.args.get('pass')
    validation(username, password)  #chcek if username and password exists in DB
    return render_template('dashboard.html')

def validation(username, password):
    pass

@app.route('/addEvent')
def addEvent():
    time = request.args.get('time')
    date = request.args.get('date')
    venue = request.args.get('venue')
    #Call db from here to save this data

def cancelEvent():
    pass

def donate():
    pass