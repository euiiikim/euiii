from pico2d import *
import random
import json

boom_data_file = open('boomdata', 'r')
boom_data = json.load(boom_data_file)
boom_data_file.close()

class Boom:
    global boom_data
    image = None
    boomitem = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.speed = 10
        self.distance = 0
        if Boom.image == None:
            self.boom = load_image('boomb.png')

    def create(self):
        boom_state = {
            "boom": self.image
        }
        boom = []
        for name in boom_data:
            bo = Boom()
            bo.name = name
            bo.x, bo.y = boom_data[name]['x'], boom_data[name]['y']
            bo.state = boom_state[boom_data[name]['state']]
            boom.append(bo)

        return boom

    def update(self, frame_time):
        if Boom.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 30
        else:
            self.distance = Boom.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.boom.draw(self.x, self.y)