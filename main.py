from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["yellow", "blue", "red", "green", "purple", "orange"]
y_position = [-80, -50, -20, 10, 40, 70]
all_turtle = []
is_race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you've win.The {winner_color} turtle is the winner.")
            else:
                print(f"you've lose.The {winner_color} turtle is the winner.")

        ran_distance = random.randint(0,10)
        turtle.forward(ran_distance)


screen.exitonclick()
