from flask import Flask, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap
import os
import time
from game import *

app = Flask(__name__)
Bootstrap(app)


@app.route('/favicon.ico')
def favicon():
    print(os.path.join(app.root_path, 'static'))
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/", methods=['GET', 'POST'])
def hello():
    user_ip = request.remote_addr
    with open('Server_Log_File.log', 'w') as logfile:
            logfile.write("Got connection from user at IP address: " + user_ip + " at time: " +
                          time.strftime("%c") + "\n")
    return render_template('index.html')


@app.route('/animal', methods=['GET', 'POST'])
def animal():
    username = request.form['uname']
    user_ip = request.remote_addr
    a = set_username(user_ip, username)
    with open('Server_Log_File.log', 'a') as logfile:
            logfile.write("Got connection from user at IP address: " + user_ip + " at time: " +
                          time.strftime("%c") + " username created: " + username + "\n")
    return render_template('animal.html', uname=username)


@app.route('/home2', methods=['GET', 'POST'])
def action():
    health_a, health_b = get_health()
    user_a, user_b = get_user()
    a = request.remote_addr
    username = get_username(a)
    act = request.form['user_action']
    update = update_stats(a, act)
    anm = get_animal(a)
    hp = get_hp(a)
    b, c, d, e = get_stats(a)
    with open('Server_Log_File.log', 'a') as logfile:
            logfile.write("Got connection from user at IP address: " + a + " at time: " +
                          time.strftime("%c") + " username created: " + username + " action chosen: " + act + "\n")
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b, user_a=user_a, user_b=user_b, hp=hp, attack=b, spc_attack=c, spc_spurn=d, speed=e)


@app.route('/home', methods=['GET', 'POST'])
def index():
    hp = '300'
    a = request.remote_addr
    anm = request.form['animal_type']
    username = get_username(a)
    monster = set_animal(a, anm)
    health_a, health_b = get_health()
    c, d, e, f = get_stats(a)
    with open('Server_Log_File.log', 'a') as logfile:
            logfile.write("Got connection from user at IP address: " + a + " at time: " +
                          time.strftime("%c") + " username created: " + username + " animal chosen: " + anm + "\n")
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b, hp=hp, attack=c, spc_attack=d, spc_spurn=e, speed=f)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')


