from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race! Enter the color: ")
print(user_bet)
is_race_on=False
colors = ["red","blue","orange","pink", "green","yellow"]
y_position = [-100,-50,0,50,100,150]
all_turtle = []

# Creating 6 turtle
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        # 235 is 250 - half the width of the turtle.
        if turtle.xcor() > 235:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You won the race, The winner color is {winner_color}")
            else:
                print(f"You lose the race, The winner color is {winner_color}")
        # Make a turtle move random amount
        random_speed = random.randint(0,10)
        turtle.forward(random_speed)

screen.exitonclick()








