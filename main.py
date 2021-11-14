from flask import Flask, redirect, url_for, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import pymysql

#initalizing flask app
app = Flask(__name__)
app.secret_key = 'my secret and not your secret'


# @app.route('/aboutus')
# def about():
#     return render_template("about.html")


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


@app.route("/sms")
def sms():
    account_sid = 'ACe656e62dfa83c630b54d7c877ac48100'
    auth_token = 'ab068d7893281856f13c1d185961cc29'
    client = Client(account_sid, auth_token)

    numbers_to_message = ['+12028094943']
    for number in numbers_to_message:
        message = client.messages \
            .create(
            body='Testing 1..2..3',
            from_='+14158911938',
            to=number
        )

        # print(message.sid)
        return message.status


@app.route("/smsreply", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Reply Demo")

    return str(resp)


db = pymysql.connect(host="sql3.freemysqlhosting.net", user="sql3450941", password="I1TIEzd82P", database="sql3450941")
@app.route("/db")
def dbs():
    # db = pymysql.connect("sql3.freemysqlhosting.net", "sql3450941", "I1TIEzd82P", "sql3450941")
    cursor = db.cursor()
    sql = "SELECT * FROM Shelters"
    cursor.execute(sql)
    results = cursor.fetchall()
    return str(results)
