from pico2d import *
from MAP import *

class ZORO:
    image_init = None
    collidtime = 0
    score = 0
    RUN, JUMP, ATTACK, CRUSH, SLIDE = 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 1
        self.state = "run"
        self.jump_state = "up"
        self.hp = 1000
        self.attack_sound = load_music('music/zoro_attack.mp3')
        self.attack_sound.set_volume(30)
        self.crush_sound = load_music('music/zoro_crush.mp3')
        self.crush_sound.set_volume(30)
        self.jump_sound = load_music('music/zoro_jump.mp3')
        self.jump_sound.set_volume(30)
        if self.image_init == None:
            self.run = load_image('image/zoro_run.png')
            self.jump = load_image('image/zoro_jump1.png')
            self.attack = load_image('image/zoro_attack1.png')
            self.crush = load_image('image/zoro_crush1.png')
            self.slide = load_image('image/zoro_slide.png')
            self.hpbar = load_image('image/hp.png')

    def get_score(self):
        return self.score

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1
        if self.state == "crush":
            self.collidtime += 1
            if self.collidtime == 1:
                self.hp -= 200
                self.crush_sound.play(1)
            if (self.collidtime >= 10):
                self.state = "run"
                self.y = 90
                self.collidtime = 0
        if self.state == "slide":
            self.y = 60
        if (self.state, self.jump_state) == ("jump", "up"):
            self.jump_sound.play(1)
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
            self.attack_sound.play(1)

        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.state = "jump"
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = "attack"
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            self.state = "run"
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = "slide"
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state, self.y = "run", 90

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
        elif self.state == "crush":
            self.crush.draw(self.x, self.y)
        elif self.state == "slide":
            self.slide.draw(self.x, self.y)
        self.hpbar.draw_to_origin(0, 500, self.hp, 50)


class ZORO2:
    image_init = None
    collidtime = 0
    score = 0
    RUN, JUMP, ATTACK, CRUSH, SLIDE = 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 1
        self.state = "run"
        self.jump_state = "up"
        self.hp = 1000
        self.attack_sound = load_music('music/zoro_attack.mp3')
        self.attack_sound.set_volume(30)
        self.crush_sound = load_music('music/zoro_crush.mp3')
        self.crush_sound.set_volume(30)
        self.jump_sound = load_music('music/zoro_jump.mp3')
        self.jump_sound.set_volume(30)
        if self.image_init == None:
            self.run = load_image('image/zoro_run.png')
            self.jump = load_image('image/zoro_jump1.png')
            self.attack = load_image('image/zoro_attack1.png')
            self.crush = load_image('image/zoro_crush1.png')
            self.slide = load_image('image/zoro_slide.png')
            self.hpbar = load_image('image/hp.png')

    def get_score(self):
        return self.score

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1
        if self.state == "crush":
            self.collidtime += 1
            if self.collidtime == 1:
                self.hp -= 250
                self.crush_sound.play(1)
            if (self.collidtime >= 10):
                self.state = "run"
                self.y = 90
                self.collidtime = 0
        if self.state == "slide":
            self.y = 60
        if (self.state, self.jump_state) == ("jump", "up"):
            self.jump_sound.play(1)
            if self.y >= 150:
                self.jump_state = "down"
            self.y += 15
        if (self.state, self.jump_state) == ("jump", "down"):
            if self.y >= 100:
                self.y -= 15
        if (self.state, self.y) == ("jump", 90):
            self.state = "run"
            self.jump_state = "up"
        if self.state == "attack":
            self.y = 90
            self.attack_sound.play(1)

        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.state = "jump"
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = "attack"
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            self.state = "run"
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = "slide"
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state, self.y = "run", 90

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
        elif self.state == "crush":
            self.crush.draw(self.x, self.y)
        elif self.state == "slide":
            self.slide.draw(self.x, self.y)
        self.hpbar.draw_to_origin(0, 500, self.hp, 50)

