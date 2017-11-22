from pico2d import *
from ZORO import ZORO
running = None

zoro = None
map = None

class MAP:
    def __init__(self):
        self.image = load_image('navymap1.png')
    def draw(self):
        self.image.draw(401, 300)

def enter():
    global zoro, map
    map = MAP()
    zoro = ZORO()

def update():
    global zoro, running
    handle_updates()
    zoro.update()
    map.update()

def handle_events():
    global running, zoro
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                zoro.state = "ju"
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
                zoro.state = "run"
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                zoro.state = "att"
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
                zoro.state = "run"

def main():
    global running, zoro, map
    open_canvas()
    running = True
    while running:
        clear_canvas()
        update_canvas()
        delay(0.05)
    close_canvas()
