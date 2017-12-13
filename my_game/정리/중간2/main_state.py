import os

from pico2d import *
from ZORO import *
from MAP import *
from HURDLE import *
from JELLY import *
from score import *

import random
import game_framework
import title_state
import result

name = "MainState"

running = None
zoro = None
map = None
hurdle = None
jelly = None
score = None
ascore = 0


def crush(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global zoro, running, map, hurdle, jelly, score, font

    zoro = ZORO()
    map = MAP()
    hurdle = Hurdle1().create()
    jelly = Jelly().create()
    score = Score()
    font = load_font('ENCR10B.TTF')

def exit():
    global zoro, map, hurdle, jelly
    del(zoro)
    del(map)
    for hur in hurdle:
        hurdle.remove(hur)
        del (hur)
    del (hurdle)
    for jel in jelly:
        jelly.remove(jel)
        del (jel)
    del (jelly)


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
    global zoro, map, hurdle, jelly, ascore
    zoro.update()
    map.update(frame_time)
    for hur in hurdle:
        hur.update(frame_time)
        if crush(zoro, hur):
            zoro.state = "crush"
    for jel in jelly:
        jel.update(frame_time)
        if crush(zoro, jel):
            jelly.remove(jel)
    score.MAP_socre()
    ascore = score.score
    if zoro.hp <= 0:
        game_framework.change_state(result)
    pass



def draw_state():
    global map, zoro, hurdle, jelly
    map.draw()
    zoro.draw()
    for hur in hurdle:
        hur.draw()
    for jel in jelly:
        jel.draw()
    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))

def draw(frame_time):
    clear_canvas()
    draw_state()
    update_canvas()
    delay(0.03)


