from pico2d import *
import random
import json

ruppy_data_file = open('data/ruppydata', 'r')
ruppy_data = json.load(ruppy_data_file)
ruppy_data_file.close()



class Ruppy:
    global ruppy_data
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.speed = 10
        self.distance = 0
        self.state = "ruppy"


        if Ruppy.image == None:
            self.ruppy = load_image('image/ruppy1.png')

    def create(self):
        ruppy_state = {
            "ruppy1" : self.image
        }

        ruppy = []
        for name in ruppy_data:
            ru = Ruppy()
            ru.name = name
            ru.x = ruppy_data[name]['x']
            ru.y = ruppy_data[name]['y']
            ru.state = ruppy_state[ruppy_data[name]['state']]
            ruppy.append(ru)

        return ruppy

    def update(self, frame_time):
        if Ruppy.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 0
        else:
            self.distance = Ruppy.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.ruppy.draw(self.x, self.y)
