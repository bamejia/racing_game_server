from controller.player_key_input import title_screen_input
from controller.player_mouse_input import title_screen_mouse_input
from controller.game_choice.online_start import online_start
from view.title_screen_view import TitleScreenView
from view.window import Window
from controller.game_choice.p1_start import p1_start
from controller.game_choice.p2_start import p2_start
# from controller.player_text_input import player_text_input
from controller.game_choice.option_menu import option_menu
import pygame
import sys
import global_variables as gv

""" temporary """
import time


class Controller:
    def __init__(self):
        self.window = Window()
        self.title_screen_view = None
        self.btn_func = {
            gv.BUTTON_TEXTS[0]: lambda: p1_start(self.window),
            gv.BUTTON_TEXTS[1]: lambda: p2_start(self.window),
            gv.BUTTON_TEXTS[2]: lambda: online_start(self.window, True),
            # gv.BUTTON_TEXTS[3]: lambda: player_text_input("ENTER NAME")
            gv.BUTTON_TEXTS[3]: lambda : online_start(self.window)
            # "OPTIONS": lambda: option_menu(self.window),
            # "EXIT": lambda: [i for i in (pygame.quit(), sys.exit())]
        }

    def run(self):

        self.title_screen_view = TitleScreenView(self.window)

        while True:
            events = pygame.event.get()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            btn_hover, btn_press, btn_choice = title_screen_mouse_input(self.title_screen_view, mouse, click)

            self.title_screen_view.show_screen(btn_hover, btn_press)
            title_screen_input(events)

            if btn_choice is not None:
                self.btn_func[btn_choice]()

            # """ 1 PLAYER START chosen """
            # if btn_choice == self.btn_choice[0]:
            #     p1_start(self.window)
            # """ 2 PLAYER START chosen """
            # if btn_choice == self.btn_choice[1]:
            #     p2_start(self.window)
            # """ OPTIONS chosen """
            # if btn_choice == self.btn_choice[2]:
            #     online_start(self.window, True)
            #     # option_menu(self.window)
            # """ EXIT chosen """
            # if btn_choice == self.btn_choice[3]:
            #     online_start(self.window)
                # pygame.quit()
                # sys.exit()

            # print(self.window.clock.get_fps())

            self.window.clock.tick(120)

