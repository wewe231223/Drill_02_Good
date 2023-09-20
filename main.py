import math
from pico2d import *

open_canvas()


ch = load_image("character.png")
gr = load_image("grass.png")

def run_circle():

    print("circle")


    cx, cy, r =  800 / 2, 600 / 2, 200
    for deg in range(0, 360, 5):
        x = cy + r * math.cos(math.degrees(deg))
        y = cy + r * math.sin(math.degrees(deg))
        clear_canvas_now()
        gr.draw_now(400, 30)
        ch.draw_now(x, y)
        delay(0.01)


def run_rectangle():
    print("rectangle")
    pass

while True:
    run_circle()
    run_rectangle()




close_canvas()