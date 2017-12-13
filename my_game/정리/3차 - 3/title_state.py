import game_framework
import start_state
import main_state
import main2_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.change_state(main2_state)


def draw(frame_time):
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass
