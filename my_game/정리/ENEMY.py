from pico2d import *
import random
import json

enemy_data_file = open('data/enemydata', 'r')
enemy_data = json.load(enemy_data_file)
enemy_data_file.close()



class Enemy1:
    global enemy_data
    image = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.speed = 10
        self.distance = 0
        self.frame = 1


        if Enemy1.image == None:
            self.enemy1 = load_image('image/enemy12.png')

    def create(self):
        enemy1_state = {
            "enemy1" : self.image
        }

        enemy = []
        for name in enemy_data:
            en = Enemy1()
            en.name = name
            en.x = enemy_data[name]['x']
            en.y = enemy_data[name]['y']
            en.state = enemy1_state[enemy_data[name]['state']]
            enemy.append(en)

        return enemy


    def update(self, frame_time):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1
        if Enemy1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 30
        else:
            self.distance = Enemy1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.enemy1.draw(self.x, self.y)
