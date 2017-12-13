from pico2d import *

class MAP:
    image_init = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.map1_x, self.map1_y = 400, 400
        self.map2_x, self.map2_y = 1200, 400
        self.map3_x, self.map3_y = 3600, 400
        self.frame = 1
        self.speed = 5
        self.distance = 0
        self.count = 0
        self.bgm = load_music('stage1_music.mp3')
        self.bgm.set_volume(40)
        self.bgm.repeat_play()

        if self.image_init == None:
            self.map1 = load_image('navymap1.png')
            self.map2 = load_image('navymap2.png')
            self.map3 = load_image('navymap3.png')

    def update(self, frame_time):
        if MAP.RUN_SPEED_PPS * frame_time > 7:
             
            self.distance = 10
        else:
            self.distance = MAP.RUN_SPEED_PPS * frame_time

        self.map1_x -= self.distance
        self.map2_x -= self.distance
        self.map3_x -= self.distance

        if self.map3_x < - 400:
            self.count += 1
            self.map3_x = 1190

        if self.map2_x < - 400:
            self.count += 1
            self.map2_x = 1190

        if self.map1_x < - 400:
            self.count += 1
            self.map1_x = 1190

        if self.count >= 4:
            self.map3_x, self.map3_y = 400, 400
            if self.frame == 5:
                self.frame = 5
            else:
                self.frame = (self.frame + 1) % 6


    def draw(self):
        self.map1.draw(self.map1_x, self.map1_y)
        self.map2.draw(self.map2_x, self.map2_y)
        self.map3.draw(self.map3_x, self.map3_y)


class MAP2:
    image_init = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.map1_x, self.map1_y = 400, 400
        self.map2_x, self.map2_y = 1200, 400
        self.map3_x, self.map3_y = 3600, 400
        self.frame = 1
        self.speed = 5
        self.distance = 0
        self.count = 0
        self.bgm = load_music('stage2_music.mp3')
        self.bgm.set_volume(40)
        self.bgm.repeat_play()

        if self.image_init == None:
            self.map1 = load_image('aronmap1.png')
            self.map2 = load_image('aronmap2.png')
            self.map3 = load_image('aronmap1.png')

    def update(self, frame_time):
        if MAP.RUN_SPEED_PPS * frame_time > 7:

            self.distance = 50
        else:
            self.distance = MAP.RUN_SPEED_PPS * frame_time

        self.map1_x -= self.distance
        self.map2_x -= self.distance
        self.map3_x -= self.distance

        if self.map3_x < - 400:
            self.count += 1
            self.map3_x = 1190

        if self.map2_x < - 400:
            self.count += 1
            self.map2_x = 1190

        if self.map1_x < - 400:
            self.count += 1
            self.map1_x = 1190

        if self.count >= 4:
            self.map2_x, self.map2_y = 400, 400
            if self.frame == 5:
                self.frame = 5
            else:
                self.frame = (self.frame + 1) % 6

    def draw(self):
        self.map1.draw(self.map1_x, self.map1_y)
        self.map2.draw(self.map2_x, self.map2_y)
        self.map3.draw(self.map3_x, self.map3_y)
