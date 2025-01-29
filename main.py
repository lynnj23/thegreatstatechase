"""This is a Quiz game to guess the 50 states of the USA and then place them on a map
It mainly tests your PANDAS ability to read a file then use SCREEN method to populate a map"""

# Imports and definitions
import turtle

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

def box_prompt():
    answer_state = screen.textinput(title="Guess a State", prompt="Input your State Guess?").lower().capitalize()
    return answer_state


def get_states():
    st_data = pd.read_csv("50_states.csv")
    return st_data


# def find_state(answer_state; data)
#     for records in states_lookup:
#         if record["state"]


# Main programme starts here
state_data = get_states()
print(state_data)
game_on = True
while game_on:
    answer_state = box_prompt()
    if answer_state in state_check:
        screen.textinput(title="Guess a State", prompt="Input your State Guess?").lower().capitalize(
    if answer_state in state_data['state'].values:

        # get the x and y co-ordinates and print the
        


# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()
