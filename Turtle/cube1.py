## Project Gabut
## Drawing a Cube with Turtle Graphics

import turtle

t = turtle.Turtle()

t.pen(pencolor="purple", pensize=5, speed=1)

def main ():
    t.hideturtle()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.goto(50, 50)
    t.right(180)
    t.forward(150)
    t.left(90)
    t.backward(90)
    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(102)
    t.left(90)
    t.goto(-50, 50)
    t.right(180)
    t.forward(103)
    
if __name__ == "__main__":
    main()
