import os

from pico2d import *
from ZORO import *
from MAP import *

import random
import game_framework
import title_state

name = "MainState"

running = None
zoro = None
map = None


def enter():
    global zoro, running, map
    zoro = ZORO()
    map = MAP()


def exit():
    global zoro, map
    del(zoro)
    del(map)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running, zoro
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            zoro.handle_event(event)
        pass


def update(frame_time):
    global zoro, map
    zoro.update()
    map.update(frame_time)
    pass



def draw_state():
    global map, zoro
    map.draw()
    zoro.draw()


def draw(frame_time):
    clear_canvas()
    draw_state()
    update_canvas()
    delay(0.03)


