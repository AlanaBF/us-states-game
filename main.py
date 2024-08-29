import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"].tolist()
x_coords = df["x"].tolist()
y_coords = df["y"].tolist()

correct_guesses = []

def write_state_on_map(state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x_coords[states.index(state)], y_coords[states.index(state)])
    t.write(state)

def update_state_list(state):
    correct_guesses.append(state)

def show_message(message):
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)
    message_turtle.color("black")
    message_turtle.write(message, align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    message_turtle.clear()

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state.lower() == "exit":
        missing_states = [state for state in states if state not in correct_guesses]
        data = {
            "States to learn": missing_states,
            "Correct guesses": correct_guesses + [""] * (len(missing_states) - len(correct_guesses))
        }
        df = pd.DataFrame(data)
        df.to_csv("states_to_learn.csv", index=False)
        print(df)
        turtle.bye()
        break
    if answer_state in states:
        if answer_state not in correct_guesses:
            show_message("Correct")
            write_state_on_map(answer_state)
            update_state_list(answer_state)
        else:
            show_message("You already guessed that")
    else:
        show_message("Incorrect")
    if len(correct_guesses) == 50:
        show_message("You got all 50 states!")

turtle.mainloop()