"""This is a Quiz game to guess the 50 states of the USA and then place them on a map
It mainly tests your PANDAS ability to read a file then use SCREEN method to populate a map"""

# Imports and definitions
import turtle
from tkinter import Image




# from operator import index

screen = turtle.Screen()
import pandas as pd

#CONSTANTS

GUESS_PROMPT = "Input your state guess?"
GUES_AGAIN = "Already entered, guess again!"
NOT_US_STATE = "Not a USA State!, guess again!"
GAME_OVER = "GAME OVER"
# set up file

image = Image.open("blank_states_img.gif")
width, height = image.size
print(f"Image width: {width} pixels, Image height: {height} pixels")

# Set up the screen
screen.title("The Great State Chase!")
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)

# Lists and constants
state_check = []


# I will set up definitions here ready for object implementation later
def get_states():
    st_data = pd.read_csv("50_states.csv")
    return st_data


def box_prompt(guess_prompt, score):
    answer_state = screen.textinput(title=f"Guess a State Score: {score}", prompt=GUESS_PROMPT).lower().capitalize()
    return answer_state

def repeat_entry(answer_state):  # Check whether state already input
    for index in range(len(state_check)):
        if state_check[index] == answer_state:
            return True

def not_usa_state(answer_state) -> object:  # This is a further trap error
    unmatched_state = state_data[state_data['state'] == answer_state]
    #print(f"TEST OUTPUT Unmatched_state - {unmatched_state}")
    return unmatched_state

def place_state(state_data, answer_state): # Places the input State onto the map
    for x in range(len(state_data)):
        print(f"Trap 3 This is the value of x = {x}")
        row = state_data.iloc[x]  # Gets the matching state row from state_data dataframe
        print(f"Trap 4 - This is value of row {row}")
        # Extract the values from the row
        if row["state"] == answer_state:
            # print(f"Trap 5 - We are in the IF statement comparing row and answer state")
            state_name = row['state']
            # print(f"Trap 6 the value of state_name only {state_name}")
            x_coordinate = int(row['x'])
            y_coordinate = int(row['y'])
            print(f"Trap 11 These are the next x and y co-ords {x_coordinate, y_coordinate}")
            turtle.penup()
            turtle.goto(x_coordinate, y_coordinate)
            turtle.write(state_name, align="center", font=("Ariel", 8, "normal"))
    return


# Main programme starts here
state_data = get_states()  # gets the data from pandas read of 50 States.csv
print(state_data)  # remove at end of programming
game_on = True
score = 0 
# found = False  # check on previous entries


while game_on:

    answer_state = box_prompt(GUESS_PROMPT, score)  # prompts for first entry
    # print(f"Trap #1 - This is the input state: {answer_state}")
    # two input error trap tests

    repeat_state = repeat_entry(answer_state)  # sends for the repeat entry procedure
    not_state = not_usa_state(answer_state)  # sends for the test 'not a USA state' procedure

    if repeat_state:  # checks output from the state entry check, if true prompts new entry
        state_check.append(answer_state)
        screen.textinput(title=f"Guess a State Score:{score}", prompt=GUES_AGAIN).lower().capitalize()
    elif not_state.empty:
        screen.textinput(title=f"Guess a State Score:{score}", prompt=NOT_US_STATE).lower().capitalize()
    else:
        place_state(state_data,answer_state)
        score += 1

    # now check to see if the game is over by comparing states input with state_data
    all_states = set(state_data['state'])
    unique_guessed_states = sorted(set(state_check))
    if unique_guessed_states == all_states:
        print("Trap 10 - got here")
        Game_on: bool = False

answer_state = screen.textinput(title="Guess a State", prompt=GAME_OVER).lower().capitalize()
turtle.mainloop()
