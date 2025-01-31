"""This is a Quiz game to guess the 50 states of the USA and then place them on a map
It mainly tests your PANDAS ability to read a file then use SCREEN method to populate a map"""

# Imports and definitions
import turtle
from operator import index

screen = turtle.Screen()
import pandas as pd

# Set up the screen
screen.title("The Great State Chase!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Lists and constants
state_check = []


# I will set up definitions here ready for object implementation later

def box_prompt(guess_prompt):
    answer_state = screen.textinput(title="Guess a State", prompt=guess_prompt).lower().capitalize()
    return answer_state


def get_states():
    st_data = pd.read_csv("50_states.csv")
    return st_data


def check_entry(answer_state):  # Check whether state already input

    for index in range(len(state_check)):
        if state_check[index] == answer_state:
            return True


# Main programme starts here

guess_prompt = "Input your state guess?"
guess_again = "Already entered, guess again!"

state_data = get_states()
print(state_data)
game_on = True
found = False  # check on previous entries
while game_on:
    answer_state = box_prompt(guess_prompt)  # prompts for first entry
    input_check = check_entry(answer_state)

    if input_check:  # checks output from the state entry check, if true prompts new entry
        state_check.append(answer_state)
        print(state_check)
        screen.textinput(title="Guess a State", prompt=guess_again).lower().capitalize()
    else: # now I need to read the file for the position

# if answer_state in state_data['state'].values:

# get the x and y co-ordinates and print the

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


        turtle.mainloop()
