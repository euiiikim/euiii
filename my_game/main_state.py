from pico2d import *
import os
import game_framework
import title_state

name = "ZORO"

running = None
zoro = None

current_time = 0.0

def pause():
    pass


def resume():
    pass

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

class ZORO:
    image_init = None

    RUN, JUMP, ATTACK = 1, 2, 3

    def __init__(self):
        self.x, self.y = 50, 90
        self.frame = 1
        self.state = self.RUN
        if self.image_init == None:
            self.RUN = load_image('image\\zoro_run.png')
            self.JUMP = load_image('image\\zoro_jump1.png')
            self.ATTACK = load_image('image\\zoro_attack1.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.state = self.JUMP
            self.y += 100
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.ATTACK
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            self.state = self.RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            self.state = self.RUN
            self.y -= 100
        pass

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1
        pass

    def draw(self):
        if self.state == self.RUN:
            self.RUN.clip_draw(self.frame * 160, 0, 160, 150, 50, self.y)
        elif self.state == self.JUMP:
            self.JUMP.draw(50, self.y)
        elif self.state == self.ATTACK:
            self.ATTACK.draw(50, self.y)

class MAP:
    global zoro, running
    def __init__(self):
        self.x, self.y = 402, 300
        self.image = load_image('image\\map.png')
    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    global zoro
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            zoro.handle_event(event)
        pass


def main():
    open_canvas()

    global zoro
    global running

    zoro = ZORO()
    map = MAP()

    running = True
    while running:
        frame_time = get_frame_time()
        handle_events()
        zoro.update()
        clear_canvas()
        map.draw()
        zoro.draw()
        update_canvas()
    delay(0.05)


if __name__ == '__main__':
    main()