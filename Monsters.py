import json

input_file = open('user_data', 'r')
q = json.load(input_file)

class Snake:
    def __init__(self, index):
        self.name = 'Snake'
        self.hp = q['user'][0]['health']
        self.attack = 7
        self.speed = 8
        self.defense = 5
        self.spc_attack = 21
        self.spc_spurn = 7

    def isAttacked(self, health):
        q['user'][0]['health'] = q['user'][0]['health'] - 30
        return(q['user'][0]['health'])

    def getAttackInfo(self):
        return self.speed,



class Rabbit:
    def __init__(self, index):
        self.name = 'Rabbit'
        self.hp = 300
        self.attack = 4
        self.speed = 10
        self.defense = 7
        self.spc_attack = 30
        self.spc_spurn = 4


class Lion:
    def __init__(self, index):
        self.name = 'Lion'
        self.hp = 300
        self.attack = 8
        self.speed = 7
        self.defense = 3
        self.spc_attack = 24
        self.spc_spurn = 8


class Dragon:
    def __init__(self, index):
        self.name = 'Dragon'
        self.hp = 300
        self.attack = 10
        self.speed = 4
        self.defense = 2
        self.spc_attack = 30
        self.spc_spurn = 10
