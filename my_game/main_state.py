from pico2d import *


def handle_events():
    global running
    global controll
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            controll.handle_event(event)
    pass

open_canvas()
map = load_image('navymap3.png')
character = load_image('zoro_run.png')

running = True
x = 0
frame = 0
while (x < 800 and running):
    clear_canvas()
    map.draw(401, 299)
    character.clip_draw(frame * 160, 0, 160, 150, x, 90)
    update_canvas()
    frame = (frame + 1) % 6
    x += 40
    delay(0.1)
    handle_events()

close_canvas()

