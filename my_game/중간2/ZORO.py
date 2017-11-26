from pico2d import *

class ZORO:
    image_init = None
    collidtime = 0
    score = 0
    RUN, JUMP, ATTACK, CRUSH = 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 1
        self.state = "run"
        self.jump_state = "up"
        self.hp = 500
        if self.image_init == None:
            self.run = load_image('zoro_run.png')
            self.jump = load_image('zoro_jump1.png')
            self.attack = load_image('zoro_attack1.png')
            self.crush = load_image('zoro_crush1.png')
            self.hpbar = load_image('hp.png')

    def get_score(self):
        return self.score

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1
        if self.state == "crush":
            self.collidtime += 1
            if self.collidtime == 1:
                self.hp -= 50
            if (self.collidtime >= 10):
                self.state = "run"
                self.y = 90
                self.collidtime = 0
        if (self.state, self.jump_state) == ("jump", "up"):
            if self.y >= 270:
                self.jump_state = "down"
            self.y += 15
        if (self.state, self.jump_state) == ("jump", "down"):
            if self.y >= 105:
                self.y -= 15
        if (self.state, self.y) == ("jump", 90):
            self.state = "run"
            self.jump_state = "up"
        if self.state == "attack":
            self.y = 90
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.state = "jump"
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = "attack"
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            self.state = "run"

    def get_bb(self):
        return self.x - 5, self.y - 40, self.x + 25, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if self.state == "run":
            self.run.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
        elif self.state == "jump":
            self.jump.draw(self.x, self.y)
        elif self.state == "attack":
            self.attack.draw(self.x, self.y)
        self.hpbar.draw_to_origin(0, 500, self.hp, 50)
