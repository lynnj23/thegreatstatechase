"""This is a Quiz game to guess the 50 states of the USA and then place them on a map
It mainly tests your PANDAS ability to read a file then use SCREEN method to populate a map"""

# Imports and definitions
import turtle
from PIL import Image
import pandas as pd

# from operator import index

screen = turtle.Screen()

#CONSTANTS

GUESS_PROMPT = "Input your state guess?"
GUES_AGAIN = "Already entered, guess again!"
NOT_US_STATE = "Not a USA State!, guess again!"
GAME_OVER = "GAME OVER"
FILE_PATH = r"C:\Users\rljam\PycharmProjects\pythonProject\Day_25_States_Quiz\learn_these_states.csv"
# set up file

image = Image.open("blank_states_img.gif")
image_width, image_height = image.size

# Set up the screen
screen.title("The Great State Chase!")
screen.setup(width=image_width, height=image_height)
screen.bgpic("blank_states_img.gif")
screen.setworldcoordinates(-362.5, -245.5, 362.5, 245.5)
#screen.addshape(image)
#turtle.shape(image)

# Lists and constants
state_check = []


# I will set up definitions here ready for object implementation later
def get_states():
    st_data = pd.read_csv("50_states.csv")
    return st_data


def box_prompt(GUESS_PROMPT, score):
    answer_state = screen.textinput(title=f"Guess a State! Score:{score} /50", prompt=GUESS_PROMPT).title()
    return answer_state


def repeat_entry(answer_state):  # Check whether state already input
    for index in range(len(state_check)):
        if state_check[index] == answer_state:
            answer_state = screen.textinput(title=f"Guess a State, Score:{score} /50", prompt=GUES_AGAIN).title()
        else:
            return False

def not_usa_state(answer_state: str) -> bool:
    # Check if the answer_state is NOT in the state_data DataFrame
    if answer_state not in state_data['state'].values:
        screen.textinput(title=f"Guess a State, Score: {score} / 50", prompt=f"{answer_state} is not a US state!")
        return True
    return False



def place_state(state_data, answer_state):  # Places the input State onto the map
    for x in range(len(state_data)):
        row = state_data.iloc[x]  # Gets the matching state row from state_data dataframe
        # Extract the values from the row
        if row["state"] == answer_state:
            state_name = row['state']
            x_coordinate = int(row['x'])
            y_coordinate = int(row['y'])
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x_coordinate, y_coordinate)
            turtle.write(state_name, align="center", font=("Arial", 8, "normal"))
    return


# Main programme starts here
state_data = get_states()  # gets the data from pandas read of 50 States.csv
game_on = True
score = 0
# found = False  # check on previous entries


while game_on:
    # TODO This whole error trap is messy and logically error prone - correct
    answer_state = box_prompt(GUESS_PROMPT, score)  # prompts for first entry
    # two input error trap tests
    if answer_state != "exit" or "Exit":
        repeat_state = repeat_entry(answer_state)  # sends for the repeat entry procedure: Repeat_State = False
        not_state = not_usa_state(answer_state)  # sends for the test 'not a USA state' procedure
        if repeat_state == False or not_state == False:  # checks output from the state entry check, if true prompts new entry
            state_check.append(answer_state)
            place_state(state_data, answer_state)
            score = len(sorted(set(answer_state)))
    else:
        all_states = set(state_data['state'])
        # now check to see if the game is over by comparing states input with state_data
        unique_guessed_states = sorted(set(state_check))
        if unique_guessed_states == all_states:
            game_on = False
            screen.textinput(title="Game Over", prompt=GAME_OVER)

    # I want to look at the unique set of states input compare to All state to identify missing states.
    missed_states = state_data[state_data["state"].isin(state_check)]
    # capture the missing states in a CSV file and output
    missed_states.to_csv(FILE_PATH, index = False)


