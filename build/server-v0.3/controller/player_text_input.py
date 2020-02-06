from tkinter import *
import global_variables as gv
import pygame
import sys
import win32gui


def player_text_input2(display_text):
    """  Prompts the user to input text and then returns that text as a string.

    Args:
        display_text (str):  tells the user what to input

    Returns:
        str:  text input by the user

    """

    window = Tk()
    window.overrideredirect(True)   # rids the window of it's minimizing and closing options
    window.attributes('-topmost', True)

    window.grid_rowconfigure(0, weight=1)   # centers the x placement
    window.grid_columnconfigure(0, weight=1)    # centers the y placement

    window_width = round(gv.WINDOW_W / 2)
    window_length = round(gv.WINDOW_L / 8)
    window_x = round(gv.WINDOW_W * 3 / 5)
    window_y = round(gv.WINDOW_L * 2 / 5)

    geometry_dimensions = "%dx%d+%d+%d" % (window_width, window_length, window_x, window_y)

    window.geometry(geometry_dimensions)    # gives the window it's width, length, and xy placement

    user_input = StringVar()    # where there user's input is stored
    user_string_reference = [""]    # what will be returned holding the string of the user's input

    def action(reference_to_user_string):   # assigns the value of the user's input to reference param
        reference_to_user_string[0] = user_input.get()
        if reference_to_user_string[0] == '':   # if no input, changes reference to kill input window
            reference_to_user_string[0] = 'kill'

    Label(text=display_text, font=30).grid(pady=5)  # Prompts the user what to input
    input_width = round(gv.WINDOW_W/24)
    Entry(textvariable=user_input, width=input_width, justify='center').grid()  # Field where the user enters text
    Button(text="Enter", command=lambda: action(user_string_reference)).grid(pady=5)  # Button that calls action func

    while True:     # keeps the window open and listening for user input
        win = win32gui.FindWindow(None, "Racing Game")
        dimensions = win32gui.GetWindowRect(win)
        window_x = dimensions[0] + round((dimensions[2] - dimensions[0]) / 2) - round(window_width / 2)
        window_y = dimensions[1] + round((dimensions[3] - dimensions[1]) / 2) - round(window_length / 2)
        window.geometry("+%d+%d" % (window_x, window_y))
        window.update_idletasks()
        window.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        if user_string_reference != ['']:
            break

    window.destroy()    # destroys tkinter root window
    print(user_string_reference[0])
    return user_string_reference[0]    # returns the value referenced


# def player_text_input(display_text):

