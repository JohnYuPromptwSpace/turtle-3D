import turtle
import math

from essential_codes import Cube, Player, EventHandler

def update_scene():
    drawer.clear()
    for obj in world_objects:
        obj.draw(player, drawer)
    screen.update()

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0, 0)



drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.pensize(2)
drawer.color("white")



player = Player(x=0, y=0, z=0)

coords = [
    ((-300, -150, -300), (300, -50, 300))
]

world_objects = []

for coord in coords:
    world_objects.append(Cube(coord[0], coord[1]))

eventhandler = EventHandler(drawer, world_objects, player)



screen.listen()
screen.onkeypress(eventhandler.on_w, "w")
screen.onkeyrelease(eventhandler.off_w, "w")

screen.onkeypress(eventhandler.on_s, "s")
screen.onkeyrelease(eventhandler.off_s, "s")

screen.onkeypress(eventhandler.on_a, "a")
screen.onkeyrelease(eventhandler.off_a, "a")

screen.onkeypress(eventhandler.on_d, "d")
screen.onkeyrelease(eventhandler.off_d, "d")

screen.onkeypress(eventhandler.on_left, "Left")
screen.onkeyrelease(eventhandler.off_left, "Left")

screen.onkeypress(eventhandler.on_right, "Right")
screen.onkeyrelease(eventhandler.off_right, "Right")

screen.onkeypress(eventhandler.on_up, "Up")
screen.onkeyrelease(eventhandler.off_up, "Up")

screen.onkeypress(eventhandler.on_down, "Down")
screen.onkeyrelease(eventhandler.off_down, "Down")

screen.onkeypress(eventhandler.on_space, "space")


def mainloop():
    player.update()
    player.collision(world_objects)
    update_scene()
    screen.ontimer(mainloop, 16)

mainloop ()
turtle.done()