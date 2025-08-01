from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed('fastest')
        rx =random.randint(-280,280)
        ey = random.randint(-280,280)
        self.goto(rx, ey)

    def refresh(self):
        rx = random.randint(-280, 280)
        ey = random.randint(-280, 280)
        self.goto(rx, ey)