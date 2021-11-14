from flask import Flask, render_template, redirect, url_for, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donorAccess', methods=['POST', 'GET'])
def loginDonor():
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

@app.route('/authorityAccess', methods=['POST', 'GET'])
def loginAuthority():
    username = request.args.get('email')
    password = request.args.get('pass')
    validation(username, password)  #chcek if username and password exists in DB
    return render_template('dashboardAuthority.html')

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


