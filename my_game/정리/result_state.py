from pico2d import *
from score import *
from ZORO import *

import game_framework
import main_state
import main2_state


name = "ResultState"


image = None
title = None
result = None
font = None
score = None
zoro = None
ascore = None

def enter():
    global title, result, font, score, zoro
    score = Score
    zoro = ZORO()
    title = load_image('image/title.png')
    result = load_image('image/result.png')
    font = load_font('image/ENCR10B.TTF', 50)
    score = Score()


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def draw_state():
    global font, score, ascore, result
    result.draw(400, 300)
    font.draw(290, 380, 'YOUR SCORE: %3.2d' % main2_state.ascore)

def draw(frame_time):
    clear_canvas()
    draw_state()
    update_canvas()
    delay(frame_time + 5)

def update():
    pass


def pause():
    pass

def resume():
    pass