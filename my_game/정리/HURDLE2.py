from pico2d import *
import random
import json

hurdle_data_file = open('data/crushhurdle', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()



class Hurdle2:
    global hurdle_data
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


        if Hurdle1.image == None:
            self.hurdle11 = load_image('image/hurdle1.png')

    def create(self):
        hurdle_state = {
            "hurdle1" : self.image
        }

        hurdle = []
        for name in hurdle_data:
            hur = Hurdle1()
            hur.name = name
            hur.x = hurdle_data[name]['x']
            hur.y = hurdle_data[name]['y']
            hur.state = hurdle_state[hurdle_data[name]['state']]
            hurdle.append(hur)

        return hurdle


    def update(self, frame_time):
        if Hurdle1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 30
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time + 5

        self.x -= self.distance

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.hurdle11.draw(self.x, self.y)
