from Monsters import *
import json

input_file = open('user_data', 'r')
q = json.load(input_file)

m1 = Snake(0)
m2 = Snake(2)


def get_user():
    return q['user'][0]['username'], q['user'][1]['username']


def get_health():
    return q['user'][0]['health'], q['user'][1]['health']


def get_animal(user_ip):
    if q['user'][0]['user_ip'] == user_ip:
        return q['user'][0]['species']
    else:
        return q['user'][1]['species']


def set_username(user_ip, username):
    if q['user'][0]['username'] == "test name":
        q['user'][0]['username'] = username
        print(user_ip)
        q['user'][0]['user_ip'] = user_ip
        print(q['user'][0]['user_ip'])
        return q['user'][0]['user_ip'], q['user'][0]['username']
    else:
        q['user'][1]['username'] = username
        q['user'][1]['user_ip'] = user_ip
        return q['user'][1]['user_ip'], q['user'][1]['username']


def set_animal(user_ip, animal_selection):
    if q['user'][0]['user_ip'] == user_ip:
        q['user'][0]['species'] = animal_selection
        if animal_selection == 'Snake':
            m1 = Snake(0)
            print(q)
            return m1
        elif animal_selection == 'Rabbit':
            m1 = Rabbit(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn
            print(q)

            return m1
        elif animal_selection == 'Dragon':
            m1 = Dragon(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn
            print(q)
            return m1
        else:
            m1 = Lion(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn
            print(q)
            return m1
    else:
        q['user'][1]['species'] = animal_selection
        if animal_selection == 'Snake':
            m2 = Snake(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            print(q)
            return m2
        elif animal_selection == 'Rabbit':
            m2 = Rabbit(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            print(q)
            return m2
        elif animal_selection == 'Dragon':
            m2 = Dragon(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            print(q)
            return m2
        else:
            m2 = Lion(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            print(q)
            return m2


def update_stats(user_ip, user_action):
    if user_ip == q['user'][0]['user_ip']:

        if user_action == 'Attack':
            m2.hp = m2.hp - m1.attack
            q['user'][1]['health'] = m2.hp
            print(q)
            return 'updated user 2 health', m2.hp
        elif user_action == 'Wait':
            m1.hp = m1.hp + 15
            q['user'][0]['health'] = m1.hp
            print(q)
            return 'updated user 1 health', m1.hp
        else:
            m2.hp = m2.hp - m1.spc_attack
            m1.hp = m1.hp - m1.spc_spurn
            q['user'][0]['health'] = m1.hp
            q['user'][1]['health'] = m2.hp
            print(q)
            return 'user 1 health', m1.hp, 'user 2 health', m2.hp
    else:
        if user_action == 'Attack':
            m1.hp = m1.hp - m2.attack
            q['user'][0]['health'] = m1.hp
            print(q)
            return 'updated user 1 health', m1.hp
        elif user_action == 'Wait':
            m2.hp = m2.hp + 15
            q['user'][1]['health'] = m2.hp
            print(q)
            return 'updated user 2 health', m2.hp
        else:
            m1.hp = m1.hp - m2.spc_attack
            m2.hp = m2.hp - m2.spc_spurn
            q['user'][0]['health'] = m1.hp
            q['user'][1]['health'] = m2.hp
            print(q)
            return 'user 1 health', m1.hp, 'user 2 health', m2.hp