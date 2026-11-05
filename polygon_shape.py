import turtle
import random
import math
import time

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # Refresh screen manually with screen.update()

artist = turtle.Turtle()
artist.hideturtle()  # Hide turtle arrow for cleaner art


class Polygon:
    def __init__(self, x, y, sides, pen_size, color, side_length, angle, pen):
        self.x = x
        self.y = y
        self.sides = sides
        self.pensize = pen_size
        self.color = color
        self.sidelength = side_length
        self.angle = angle
        self.pen = pen

    def draw(self):
        """Moves to (x, y) and draws the polygon."""
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        self.pen.pendown()
        self.pen.pensize(self.pensize)
        self.pen.pencolor(self.color)
        
        for _ in range(self.sides):
            self.pen.forward(self.sidelength)
            self.pen.left(360 // self.sides)
            
        self.pen.penup()

    def move_to(self, x, y):
        """Updates internal coordinates."""
        self.x = x
        self.y = y


rng = random.Random(24)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]
shapes = []

# Spawn 12 distinct shapes
for _ in range(12):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)
    sides = rng.randint(3, 6)
    pen_size = rng.randint(1, 6)
    color = rng.choice(colors)
    side_length = rng.randint(35, 105)
    angle = rng.randint(0, 359)
    
    shape = Polygon(x, y, sides, pen_size, color, side_length, angle, artist)
    shapes.append((shape, x, y, rng.random() * 6.28))

# Main animation loop
for frame in range(1000):
    artist.clear()  # Erase all drawings from the previous frame
    
    for shape, home_x, home_y, phase in shapes:
        # Calculate new orbit position
        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        
        shape.move_to(x, y)
        shape.draw()  # Draw at the updated position
        
    screen.update()    # Render the complete frame
    time.sleep(0.045)  # Frame delay (~22 FPS)

screen.mainloop()