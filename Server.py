from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from game import *

app = Flask(__name__)
Bootstrap(app)


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
    health_a, health_b = get_health()
    user_a, user_b = get_user()
    a = request.remote_addr
    act = request.form['user_action']
    update = update_stats(a, act)
    anm = get_animal(a)
    print(update)
    print(act)
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b, user_a=user_a, user_b=user_b)


@app.route('/home', methods=['GET', 'POST'])
def index():
    a = request.remote_addr
    anm = request.form['animal_type']
    monster = set_animal(a, anm)
    health_a, health_b = get_health()
    print(monster)
    print(a)
    print(anm)
    return render_template('home.html', animal=anm, health_a=health_a, health_b=health_b)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


