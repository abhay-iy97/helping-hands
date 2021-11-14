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
    return redirect(url_for('dashboard'), code=307)

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('pages-profile.html')

@app.route('/events', methods=['POST', 'GET'])
def events():
    return render_template('events.html')

@app.route('/donations', methods=['POST', 'GET'])
def donations():
    return render_template('donations.html')

def validation(username, password):
    pass

@app.route('/addEvent', methods=['POST', 'GET'])
def addEvent():
    name = request.args.get('event_name')
    time = request.args.get('event_time')
    date = request.args.get('event_date')
    venue = request.args.get('event_venue')
    return name

def cancelEvent():
    pass

def donate():
    pass
