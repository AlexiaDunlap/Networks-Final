from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from game import *
import json

input_file = open('user_data', 'r')
q = json.load(input_file)
#app = ''
#q = []
#q.append({"name":"Rudy", "lastname":"Cortes"})
#print(json.dumps(q,indent=4))

app = Flask(__name__)
Bootstrap(app)

#Bootstrap(app1)

#{% extends "bootstrap_responsive.html" %}
#create_app()

#@app.route('/', methods=['GET', 'POST'])
#def login():

@app.route("/", methods=['GET', 'POST'])
def hello():
    print('initial: ' +  q['user'][0]['username'])
    return render_template('index.html')

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    username = request.form['uname']
    if q['user'][0]['username'] == "test name":
        q['user'][0]['username'] = username
        q['user'][0]['user_ip'] = request.remote_addr
    else:
        q['user'][1]['username'] = username
        q['user'][1]['user_ip'] = request.remote_addr

    print(username)
    print('user1: ' + q['user'][0]['username'])
    print('user2: ' + q['user'][1]['username'])

    return render_template('animal.html', uname = username)




@app.route('/home', methods=['GET', 'POST'])
def index():
    a = request.remote_addr
    anm = request.form['animal_type']
    monster = set_animal(a, anm)
    print(monster)
    print(a)
    print(anm)
    return render_template('home.html', animal=anm)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


