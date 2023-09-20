import math
from pico2d import *

open_canvas()


ch = load_image("character.png")
gr = load_image("grass.png")

def run_circle():
    print("circle")

    clear_canvas_now()
    gr.draw_now(400,30)
    ch.draw_now(400,90)
    delay(1)

    pass

def run_rectangle():
    print("rectangle")
    pass

while True:
    run_circle()
    run_rectangle()




close_canvas()