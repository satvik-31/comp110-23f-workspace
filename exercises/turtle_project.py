"""Drawing a scenery with turtle!"""

__author__ = "730517765"


from turtle import Turtle, colormode, done 


def main() -> None: 
    """The entry point of my scene."""
    hills: Turtle = Turtle()
    lake: Turtle = Turtle()
    draw_sun: Turtle = Turtle()
    mountain(hills, 40, 0 ,80)
    mountain(hills, -40, 0,80)
    mountain(hills, 0, 0, 80)
    mountain(hills, -120, 0, 80)
    mountain(hills, -160, 0, 80)
    mountain(hills, -200, 0, 80)
    mountain(hills, -240, 0, 80)
    mountain(hills, -280, 0, 80)
    lake(water, -200, 0, 400)
    draw_sun(sun, -200, 200)

    done()

def mountain (hills: Turtle, x: float, y: float, width: float ) -> None:
    """Draws mountains as a set of triangles."""
    hills.color("brown")
    hills.penup()
    hills.goto(x,y)
    hills.setheading(0.0)
    hills.pendown()
    i: int = 0
    while i < 3:
        hills.forward(width)
        hills.left(120)
        i = i + 1


def lake(water: Turtle, height: float, width: float) -> None: 
    """Fills whole area below the mountains with water"""
    water.colour("blue")
    water.penup()
    water.setheading(0,0)
    water.fillcolor()
    water.pendown()
    j: int = 0 
    while j < 4:
        water.forward(width)
        water.left(90)
        water.forward(height)
        water.left(90)
        j = j + 1


def draw_sun(sun: Turtle, t: float, z: float):
    sun = Turtle()
    sun.penup()
    sun.goto(150, 150)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    for _ in range(t):
        sun.forward(t)
        sun.right(z)
    sun.end_fill()

if __name__ == "__main__":
    main()    