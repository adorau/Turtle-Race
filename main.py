from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def restart():
    screen.clearscreen()
    race()


def race():
    user_choice = screen.textinput("Put your bet", "Who is the winner: "
                                                   "yellow,orange,pink,red,blue,green? Choose the color:")
    print(user_choice)

    race_start = False
    turtles = []

    kolor = ["yellow", "orange", "pink", "red", "blue", "green"]
    y = -130
    for i in range(6):
        n_turtle = Turtle(shape="turtle")
        n_turtle.color(kolor[i])
        n_turtle.penup()
        n_turtle.goto(-240,y)
        y += 50
        n_turtle.speed(10)
        turtles.append(n_turtle)

    if user_choice:
        race_start = True

    while race_start:
        for i in turtles:
            if i.xcor() < 230:
                ruch = random.randint(0, 10)
                i.forward(ruch)
            else:
                if i.xcor() >= 230 and user_choice == i.pencolor():
                    print(f"You won! {i.pencolor()} won this race. Press r to restart.")
                else:
                    print(f"You lose, {i.pencolor()} won this race. Press r to restart.")
                race_start = False

    screen.listen()
    screen.onkey(restart, "r")


race()
screen.exitonclick()
