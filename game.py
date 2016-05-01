from Monsters import *
import json

input_file = open('user_data', 'r')
q = json.load(input_file)

m1 = ''
m2 = ''

def set_animal(user_ip, animal_selection):

    if q['user'][0]['user_ip'] == user_ip:
        q['user'][0]['species'] = animal_selection
        if animal_selection == 'Snake':
            m1 = Snake(0)
            return m1
        elif animal_selection == 'Rabbit':
            m1 = Rabbit(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn

            return m1
        elif animal_selection == 'Dragon':
            m1 = Dragon(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn
            return m1
        else:
            m1 = Lion(0)
            q['user'][0]['health'] = m1.hp
            q['user'][0]['attack'] = m1.attack
            q['user'][0]['speed'] = m1.speed
            q['user'][0]['defense'] = m1.defense
            q['user'][0]['spc_attack'] = m1.spc_attack
            q['user'][0]['spc_spurn'] = m1.spc_spurn
            return m1
    else:
        if animal_selection == 'Snake':
            m2 = Snake(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            return m2
        elif animal_selection == 'Rabbit':
            m2 = Rabbit(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            return m2
        elif animal_selection == 'Dragon':
            m2 = Dragon(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            return m2
        else:
            m2 = Lion(1)
            q['user'][1]['health'] = m2.hp
            q['user'][1]['attack'] = m2.attack
            q['user'][1]['speed'] = m2.speed
            q['user'][1]['defense'] = m2.defense
            q['user'][1]['spc_attack'] = m2.spc_attack
            q['user'][1]['spc_spurn'] = m2.spc_spurn
            return m2