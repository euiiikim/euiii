from pico2d import *
import random
import json

crr_data_file = open('crrdata', 'r')
crr_data = json.load(crr_data_file)
crr_data_file.close()
crr2_data_file = open('crrdata2', 'r')
crr2_data = json.load(crr2_data_file)
crr2_data_file.close()

class Crr:
    global crr_data
    image = None
    crritem = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.speed = 10
        self.distance = 0
        self.crr_sound = load_music('jelly.mp3')
        self.crr_sound.set_volume(30)
        if Crr.image == None:
            self.crr = load_image('crr.png')

    def create(self):
        crr_state = {
            "crr": self.image
        }
        crr = []
        for name in crr_data:
            cr = Crr()
            cr.name = name
            cr.x, cr.y = crr_data[name]['x'], crr_data[name]['y']
            cr.state = crr_state[crr_data[name]['state']]
            crr.append(cr)

        return crr

    def update(self, frame_time):
        if Crr.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 30
        else:
            self.distance = Crr.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.crr.draw(self.x, self.y)


class Crr2:
    global crr_data
    image = None
    crritem = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.speed = 10
        self.distance = 0
        self.crr_sound = load_music('jelly.mp3')
        self.crr_sound.set_volume(30)
        if Crr2.image == None:
            self.crr2 = load_image('crr.png')

    def create(self):
        crr2_state = {
            "crr2": self.image
        }
        crr2 = []
        for name in crr2_data:
            cr = Crr2()
            cr.name = name
            cr.x, cr.y = crr2_data[name]['x'], crr2_data[name]['y']
            cr.state = crr2_state[crr2_data[name]['state']]
            crr2.append(cr)

        return crr2

    def update(self, frame_time):
        if Crr2.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 30
        else:
            self.distance = Crr2.RUN_SPEED_PPS * frame_time + 20

        self.x -= self.distance

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.crr2.draw(self.x, self.y)