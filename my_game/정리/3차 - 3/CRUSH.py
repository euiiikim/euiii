from pico2d import*
import random
import json

hudle_data_file = open('navymap1', 'r')
hudle_data = json.load(crushhudle_data_file)
crushhudle_data_file.close()

class crushhudle:
    global hudle_data
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

        if hudle1.image == None:
            self.hudle1 = load_image('hudle1.png')

    def create(self):
        hurdle_state = {
            "hurdle1": self.image
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
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def draw(self):
        self.hurdle11.draw(self.x, self.y)

