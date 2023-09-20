import math
from pico2d import *

open_canvas()


ch = load_image("character.png")
gr = load_image("grass.png")


def render_all(x = int,y = int):
    clear_canvas_now()
    gr.draw_now(400, 30)
    ch.draw_now(x, y)
    delay(0.01)




def run_circle():
    print("circle")
    cx, cy, r =  400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.degrees(deg))
        y = cy + r * math.sin(math.degrees(deg))
        render_all(x,y)


def run_rectangle():

    #bottom line
    # for x in range(50, 750+1, 10):
    #     render_all(x,90)
    #     pass


    #right side up
    # for y in range(100,550+1,10):
    #     render_all(30,y)
    #





    #top line
    # for x in range(750, 50 - 1, -10):
    #     render_all(x,550)
    #     pass



    #right side up
    for y in range(550,100 - 1,-10):
        render_all(20, y)
        pass




    print("rectangle")
    pass



while True:
    #run_circle()
    run_rectangle()




close_canvas()