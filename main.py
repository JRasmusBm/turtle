import turtle

class Directions:
    def __init__(self, turn_speed_constant, move_speed_constant):
        self._turn_speed_constant = turn_speed_constant
        self._move_speed_constant = move_speed_constant
        self.turn_speed = 0
        self.move_speed = 0

    def right(self):
        self.turn_speed += self._turn_speed_constant

    def left(self):
        self.turn_speed -= self._turn_speed_constant

    def forward(self):
        self.move_speed += self._move_speed_constant

    def backward(self):
        self.move_speed -= self._move_speed_constant

directions = Directions(turn_speed_constant=30, move_speed_constant=15)

screen = turtle.getscreen()

screen.onkeypress(key="w", fun=directions.forward)
screen.onkeypress(key="s", fun=directions.backward)
screen.onkeypress(key="a", fun=directions.left)
screen.onkeypress(key="d", fun=directions.right)

screen.onkeyrelease(key="w", fun=directions.backward)
screen.onkeyrelease(key="s", fun=directions.forward)
screen.onkeyrelease(key="a", fun=directions.right)
screen.onkeyrelease(key="d", fun=directions.left)

screen.listen()

def tick():
    turtle.right(directions.turn_speed)
    turtle.forward(directions.move_speed)
    turtle.ontimer(fun=tick, t=100)

tick()

screen.mainloop()
