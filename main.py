import math
from pico2d import *

open_canvas()


ch = load_image("character.png")
gr = load_image("grass.png")

def run_circle():
    print("circle")
    cx, cy, r =  400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.degrees(deg))
        y = cy + r * math.sin(math.degrees(deg))
        clear_canvas_now()
        gr.draw_now(400, 30)
        ch.draw_now(x, y)
        delay(0.1)


def run_rectangle():

    #bottom line
    for x in range(50, 750+1, 10):
    
        clear_canvas_now()
        gr.draw_now(400, 30)
        ch.draw_now(x, 90)
        delay(0.1)
        pass

    print("rectangle")
    pass



while True:
    #run_circle()
    run_rectangle()




close_canvas()