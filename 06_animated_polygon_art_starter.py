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
artist.hideturtle()

class polygon:
    def __init__(self,x, y, sides,pen_size,color,side_length,angle,pen):
        self.x = x
        self.y = y
        self.sidelength = side_length
        self.color = color
        self.pensize = pen_size
        self.sides = sides
        self.angle = angle
        self.pen = pen

        #Instantiation

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

        #draw a polygon 3 to N sides

    def move_to(self,x,y):
        self.pen.teleport(x,y)

        #teleportation enderman

rng = random.Random(12)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"] #allowed colours
shapes = []

for i in range(12):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)
    sides = rng.randint(3, 6)
    pen_size = rng.randint(1, 6)
    color = rng.choice(colors)
    side_length = rng.randint(35, 105)
    angle = rng.randint(0, 359)
    
    shape = polygon(x, y, sides, pen_size, color, side_length, angle, artist) #create shape object
    shapes.append((shape, x, y, rng.random() * 6.28)) #append shape object into a list

for frame in range(10000): #10000 ticks
    artist.clear() #clear the board for the next frame operation

    for shape, home_x, home_y, phase in shapes: # loop through the list of shapes
        x = home_x + 32 * math.cos(frame * 0.07 + phase) # apply a movement to it on x and y axis
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        shape.move_to(x, y) # teleport to the desired location set in list  
        shape.draw() #draw the shape

    screen.update() # update the frame
    time.sleep(0.045) #delay

screen.mainloop()