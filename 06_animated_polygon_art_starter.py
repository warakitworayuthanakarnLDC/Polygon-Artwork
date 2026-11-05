"""EXERCISE: animate multiple polygons by moving existing objects.
First finish polygon_shape.py. Then change the motion, colors, sizes,
number of polygons, and frame count to create your own artwork.
"""
import turtle
import random
import math
import time


screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0) 
artist = turtle.Turtle()
artist.shape("arrow")
artist.pencolor("black")


class polygon:
    def __init__(self,x, y, sides,pen_size,color,side_length,angle,pen):
        self.x=x
        self.y=y
        self.sidelength=side_length
        self.color=color
        self.pensize=pen_size
        self.sides=sides
        self.angle=angle
        self.pen=pen

    def draw(self):
        i=0
        self.pen.pendown()
        self.pen.pensize(self.pensize)
        self.pen.pencolor(self.color)
        self.pen.setheading(self.angle)
        while i < self.sides:
            self.pen.forward(self.sidelength)
            self.pen.left(360//self.sides)
            i+=1
        self.pen.penup()

    def move_to(self,x,y):
        self.pen.teleport(x,y)

rng = random.Random(24)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]
shapes = []
for _ in range(1):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)
    shape = polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),rng.choice(colors), rng.randint(1, 6), rng.randint(0, 359),artist)
    shape.draw()
    artist.teleport(x,y)
    shapes.append((shape, x, y, rng.random() * 6.28))

for frame in range(10000):
    artist.clear()
    for shape, home_x, home_y, phase in shapes:
        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        shape.move_to(x, y) 
        shape.draw()
    screen.update()
    time.sleep(0.045) 

screen.mainloop()