import turtle
import random

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # We draw the whole scene before refreshing the screen.
artist = turtle.Turtle()
artist.shape("arrow")
artist.pencolor("black")

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]
rng = random.Random(12)


class polygon:
    def __init__(self,x, y, side_length, color, pen_size,sides,angle,pen):
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


polygons = []  # Hold references so the Polygon objects remain accessible.
for _ in range(15):
    sides = rng.randint(3, 6)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(1,360)
    distance = rng.randint(100,200)
    polygon_shape = polygon(x, y, side_length, color, pen_size,sides,angle,artist)
    polygon_shape.draw()
    polygon_shape.move_to(x,y)
    polygons.append(polygon_shape)

screen.update()
screen.mainloop()