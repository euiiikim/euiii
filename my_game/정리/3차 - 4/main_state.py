import os

from pico2d import *
from ZORO import *
from MAP import *
from RUPPY import *
from HURDLE import *
from JELLY import *
from score import *
from BOOM import *
from Crr import *
from ALCH import *
from ENEMY import *


import random
import game_framework
import title_state
import result_state
import main2_state


name = "MainState"

enemy1 = None
ruppy = None
running = None
zoro = None
map = None
hurdle = None
boom = None
jelly = None
score = None
crr = None
alch = None
ascore = 0
jelly_sound = None
alch_sound = None
crr_sound = None

def crush(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global alch, zoro, running, map, hurdle, jelly, score, font, ruppy, boom, crr, jelly_sound, alch_sound, crr_sound, enemy1
    zoro = ZORO()
    map = MAP()
    enemy1 = Enemy1().create()
    alch = Alch().create()
    crr = Crr().create()
    boom = Boom().create()
    ruppy = Ruppy().create()
    hurdle = Hurdle1().create()
    jelly = Jelly().create()
    score = Score()
    font = load_font('ENCR10B.TTF')
    jelly_sound = Jelly()
    alch_sound = Alch()
    crr_sound = Crr()

def exit():
    global zoro, map, hurdle, jelly, ruppy, boom, crr, alch, enemy1
    del(zoro)
    del(map)
    for en in enemy1:
        enemy1.remove(en)
        del (en)
    del (enemy1)
    for al in alch:
        alch.remove(al)
        del (al)
    del (alch)
    for cr in crr:
        crr.remove(cr)
        del (cr)
    del (crr)
    for bo in boom:
        boom.remove(bo)
        del (bo)
    del (ruppy)
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
    global running, zoro, map
    if map.frame >= 5:
        game_framework.change_state(main2_state)
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
    global zoro, map, hurdle, jelly, ascore, ruppy, boom, crr, alch, score, enemy1
    zoro.update()
    map.update(frame_time)
    for en in enemy1:
        en.update(frame_time)
        if crush(zoro, en) and zoro.state == "run":
            zoro.state = "crush"
            zoro.hp -= 50
        elif crush(zoro, en) and zoro.state == "attack":
            enemy1.remove(en)
            score.score += 300
    for al in alch:
        al.update(frame_time)
        if crush(zoro, al):
            alch_sound.alch_sound.play()
            alch.remove(al)
            zoro.hp += 100
    for cr in crr:
        cr.update(frame_time)
        if crush(zoro, cr):
            crr_sound.crr_sound.play()
            crr.remove(cr)
            score.score += 300
    for bo in boom:
        bo.update(frame_time)
        if crush(zoro, bo):
            zoro.state = "crush"
            score.score -= 300
    for hur in hurdle:
        hur.update(frame_time)
        if crush(zoro, hur):
            zoro.state = "crush"
            score.score -= 300
    for jel in jelly:
        jel.update(frame_time)
        if crush(zoro, jel):
            jelly_sound.jelly_sound.play()
            jelly.remove(jel)
            score.score += 150
    for ru in ruppy:
        ru.update(frame_time)
        if crush(zoro, ru):
            ruppy.remove(ru)
            score.score += 5000
    score.MAP_socre()
    ascore = score.score
    if zoro.hp <= 0:
        game_framework.change_state(result_state)
    pass



def draw_state():
    global map, zoro, hurdle, jelly, ruppy, boom, crr, alch, enemy1
    map.draw()
    zoro.draw()
    for en in enemy1:
        en.draw()
    for al in alch:
        al.draw()
    for cr in crr:
        cr.draw()
    for bo in boom:
        bo.draw()
    for hur in hurdle:
        hur.draw()
    for jel in jelly:
        jel.draw()
    for ru in ruppy:
        ru.draw()
    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))

def draw(frame_time):
    clear_canvas()
    draw_state()
    update_canvas()
    delay(0.03)


