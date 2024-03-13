from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(800, 550)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win this race? Enter a color: ")
# print(user_bet)

color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = 150

for turtle in color:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y)
    new_turtle.color(turtle)
    y -= 50
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_dist = randint(0, 10)
        turtle.speed("fastest")
        turtle.fd(rand_dist)


screen.exitonclick()