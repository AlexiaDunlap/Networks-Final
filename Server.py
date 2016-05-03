from flask import Flask, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap
import os
from game import *

app = Flask(__name__)
Bootstrap(app)


@app.route('/favicon.ico')
def favicon():
    print(os.path.join(app.root_path, 'static'))
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


@app.route('/animal2', methods=['GET', 'POST'])
def animal2():
    reset_monster()
    a = request.remote_addr
    username = get_username(a)
    return render_template('animal.html', uname=username)


@app.route('/animal', methods=['GET', 'POST'])
def animal():
    username = request.form['uname']
    user_ip = request.remote_addr
    a = set_username(user_ip, username)
    print(a)
    print('finished loading /animal')
    return render_template('animal.html', uname=username)


@app.route('/home2', methods=['GET', 'POST'])
def action():
    health_a, health_b = get_health()
    user_a, user_b = get_user()
    a = request.remote_addr
    act = request.form['user_action']
    update = update_stats(a, act)
    anm = get_animal(a)
    hp = get_hp(a)
    b, c, d, e = get_stats(a)
    print(update)
    print(act)
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b, user_a=user_a, user_b=user_b, hp=hp, attack=b, spc_attack=c, spc_spurn=c, speed=e)


@app.route('/home', methods=['GET', 'POST'])
def index():
    print('started loading /home')
    hp = '300'
    print('hp initialize')
    a = request.remote_addr
    print(a)
    anm = request.form['animal_type']
    print('3')
    monster = set_animal(a, anm)
    print('4')
    health_a, health_b = get_health()
    print('5')
    c, d, e, f = get_stats(a)
    print('finished loading /home')
    print(monster)
    print(a)
    print(anm)
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b, hp=hp, attack=c, spc_attack=d, spc_spurn=e, speed=f)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')


