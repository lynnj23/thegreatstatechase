"""This is a Quiz game to guess the 50 states of the USA and then place them on a map
It mainly tests your PANDAS ability to read a file then use SCREEN method to populate a map"""

# Imports and definitions
import turtle
from operator import index

screen = turtle.Screen()
import pandas as pd

#CONSTANTS

guess_prompt = "Input your state guess?"
guess_again = "Already entered, guess again!"



# Set up the screen
screen.title("The Great State Chase!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Lists and constants
state_check = ['Ohio']


# I will set up definitions here ready for object implementation later

def box_prompt(guess_prompt):
    answer_state = screen.textinput(title="Guess a State", prompt=guess_prompt).lower().capitalize()
    return answer_state


def get_states():
    st_data = pd.read_csv("50_states.csv")
    return st_data


def repeat_entry(answer_state):  # Check whether state already input

    for index in range(len(state_check)):
        if state_check[index] == answer_state:
            return True

def not_usa_state():


# Main programme starts here
state_data = get_states() # gets the data from pandas read of 50 States.csv
print(state_data)
game_on = True
found = False  # check on previous entries

while game_on:
    answer_state = box_prompt(guess_prompt)  # prompts for first entry
    print(f"This is the input state: {answer_state}")
    input_check = repeat_entry(answer_state)

    if input_check:  # checks output from the state entry check, if true prompts new entry
        state_check.append(answer_state)
        print(state_check)
        screen.textinput(title="Guess a State", prompt=guess_again).lower().capitalize()
    else:


# if answer_state in state_data['state'].values:

# get the x and y co-ordinates and print the

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


        turtle.mainloop()
