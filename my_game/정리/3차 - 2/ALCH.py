from pico2d import *
import random
import json

alch_data_file = open('alchdata', 'r')
alch_data = json.load(alch_data_file)
alch_data_file.close()

class Alch:
    global alch_data
    image = None
    alchitem = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.speed = 10
        self.distance = 0
        self.alch_sound = load_music('jelly.mp3')
        self.alch_sound.set_volume(30)
        if Alch.image == None:
            self.alch = load_image('alch.png')

    def create(self):
        alch_state = {
            "alch": self.image
        }
        alch = []
        for name in alch_data:
            al = Alch()
            al.name = name
            al.x, al.y = alch_data[name]['x'], alch_data[name]['y']
            al.state = alch_state[alch_data[name]['state']]
            alch.append(al)

        return alch

    def update(self, frame_time):
        if Alch.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 100
        else:
            self.distance = Alch.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.alch.draw(self.x, self.y)