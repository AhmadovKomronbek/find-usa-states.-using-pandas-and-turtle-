import turtle
import pandas
image = "blank_states_img.gif"

# Screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.addshape(image)
turtle.shape(image)

# Turtle
my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.shape("circle")
my_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
my_turtle.penup()
my_turtle.speed("fastest")

# Main code
states_find = []
data = pandas.read_csv("50_states.csv")

while len(states_find) < 50:
    states_name = screen.textinput(f"{len(states_find)}/50", "Enter state name or exit:")
    if states_name.lower() == "exit":
        break
    if any(data["state"] == states_name):
        if states_name not in states_find:
            stats_loc = data[data["state"] == states_name]
            my_turtle.goto(int(stats_loc["x"].values[0]), int(stats_loc["y"].values[0]))
            my_turtle.color("black")
            my_turtle.write(states_name, align="center")
            my_turtle.color("red")
            states_find.append(states_name)

screen.exitonclick()
