from flask import Flask, redirect, url_for, render_template, request
import requests
import urllib

#initalizing flask app
app = Flask(__name__)
app.secret_key = 'my secret is my secret none of your secret'


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