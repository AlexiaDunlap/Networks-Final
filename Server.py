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
monster = ''
#Bootstrap(app1)

#{% extends "bootstrap_responsive.html" %}
#create_app()

#@app.route('/', methods=['GET', 'POST'])
#def login():

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    username = request.form['uname']
    user_ip = request.remote_addr
    a = set_username(user_ip, username)
    print(a)
    return render_template('animal.html', uname=username)

@app.route('/home2', methods=['GET', 'POST'])
def action():
    a = request.remote_addr
    act = request.form['user_action']
    update = update_stats(a, act)
    anm = get_animal(a)
    print(update)
    print(act)
    return render_template('home.html', animal=anm)


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


