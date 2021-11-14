from flask import Flask, redirect, url_for, render_template, request
import requests
import urllib
import pymysql
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

#initalizing flask app
app = Flask("__name__")
app.secret_key = 'my secret and not your secret'


# @app.route('/aboutus')
# def about():
#     return render_template("about.html")

db = pymysql.connect(host="sql3.freemysqlhosting.net", user="sql3450941", password="I1TIEzd82P", database="sql3450941")
account_sid = 'ACe656e62dfa83c630b54d7c877ac48100'
auth_token = 'xxx'  #change to correct token here
client = Client(account_sid, auth_token)
# @app.route('/aboutus')
# def about():
#     return render_template("about.html")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/location', methods=['POST', 'GET'])
def location():
    print("in location", flush=True)
    app.logger.info("in location")
    app.logger.warning("in location")
    app.logger.error("in location")

    # year = request.args.get('year')
    zipCode = request.args.get('zipCode')
    app.logger.warning("zipcode", zipCode)
    # date = request.args.get('date')
    url = 'http://dev.virtualearth.net/REST/v1/Locations?' 
    key = 'Ak7iTQXGfzgqJSIaOPYxLU4VGFA0yiVwXFgFUAhUfEtqBd_SuKzcKMhAmGN2fq9n'
    cr = 'US'
    results = url + urllib.parse.urlencode(({'CountryRegion': cr, 'postalCode': zipCode, 'key': key}))
    response = requests.get(results)
    print("response : ", response)
    parser = response.json()
    auth = parser['statusDescription']
    if auth == 'OK':
        # if 'adminDistrict' not in parser['resourceSets'][0]['resources'][0]['address']:
            # return 'Location does not exist in US! Please try again!'
        # state = parser['resourceSets'][0]['resources'][0]['address']['adminDistrict']
        lat = parser['resourceSets'][0]['resources'][0]['point']['coordinates'][0]
        lon = parser['resourceSets'][0]['resources'][0]['point']['coordinates'][1]

        x1 = parser['resourceSets'][0]['resources'][0]['bbox'][0]
        y1 = parser['resourceSets'][0]['resources'][0]['bbox'][1]
        x2 = parser['resourceSets'][0]['resources'][0]['bbox'][2]
        y2 = parser['resourceSets'][0]['resources'][0]['bbox'][3]

        # app.logger.warn("latitute and longitute", lat, lon, ".")
        city = parser['resourceSets'][0]['resources'][0]['address']['locality']
        return redirect(url_for('index', city=city, latitude=lat, longitude=lon))
    else:  
        return 'Status: %s! Server issue! Please try again later!' % auth

@app.route('/donorAccess', methods=['POST', 'GET'])
def login():
    username = request.args.get('email')
    password = request.args.get('pass')
    validation(username, password)  #chcek if username and password exists in DB
    return redirect(url_for('dashboard'), code=307)

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    cursor = db.cursor()
    sql = "Select * from Zipcodes limit 3;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # return toJson(results)
    count = 41290
    return render_template('dashboard.html',result = results, count = count)


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
    # Numbers from db in the same zipcode
    numbers_to_message = ['+12028094943']
    for number in numbers_to_message:
        message = client.messages \
            .create(
            body='Event ' + str(name) + ' near You. Please reply Yes to confirm. Otherwise ignore.',
            from_='+14158911938',
            to=number
        )

    #     # print(message.sid)
    #     # return message.status

    return render_template('event_created.html')


@app.route("/smsreply", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    if body == 'Yes':
        resp.message("Thank You for your registration.")

    return str(resp)

@app.route('/maps', methods=['POST', 'GET'])
def maps():
    cursor = db.cursor()
    sql = "Select * from Zipcodes limit 3;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # return toJson(results)

    return render_template('maps-google.html', result = results)

@app.route('/authorityAccess', methods=['POST', 'GET'])
def authorityAccess():
    username = request.args.get('email')
    password = request.args.get('pass')
    validation(username, password)  #chcek if username and password exists in DB
    cursor = db.cursor()
    sql = "Select * from Zipcodes limit 3;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # return toJson(results)
    count = 41290
    return render_template('dashboardAuthority.html', result = results, count = count )

@app.route('/donated', methods=['POST', 'GET'])
def donated():
    return render_template('donated.html')

def cancelEvent():
    pass

def donate():
    pass