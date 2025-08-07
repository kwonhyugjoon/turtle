from pico2d import *

open_canvas()

player = load_image('character.png')
grass = load_image('grass.png')

i = 0
while(i < 800):
    clear_canvas_now()
    player.draw_now(i,90)
    grass.draw_now(400,30)
    i = i + 10
    delay(0.2)

close_canvas()
