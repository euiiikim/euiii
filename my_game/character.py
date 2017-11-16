from pico2d import *

class CHARACTER:
    image_init = None
    state_init = None
    crushtime = 0
    score = 0
    def __init__(self):
        self.x = 10
        self.y = 90
        self.frame = 1
        self.state = "run"
        self.jump_state = "up"
        self.attack_state = "attack"
        self.hp = 500
        self.score = 0

    if self.image_init == None:
        self.run = load_image('zoro_run.png')
        self.jump = load_image('zoro_jump.png')
        self.attack = load_image('zoro_attack.png')
        self.crush = load_image('zoro_crush.png')
        self.hpbar = load_image('hp.png')

    def heal(self):
        self.hp += 100

    def update(self):
        self.hp -= 1
        self.frame += 1

    def draw(self):
        if self.state == "run":
            self.run.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
        elif self.state == "jump":
            self.jump.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
        elif self.state == "attack":
            self.attack.draw(self.frame * 160, 0, 160, 150, self.x, self.y)
        elif self.state == "crush":
            self.crush.draw(self.frame * 160, 0, 160, 150, self.x, self.y)
        self.hpbar.draw_to_origin(0, 500, self.hp, 50)