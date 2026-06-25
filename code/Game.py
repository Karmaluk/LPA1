#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.GameOver import GameOver
from code.Victory import Victory
from code.About import About


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Dark Forest')

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

                if level_return == 'game_over':
                    GameOver(self.window).run()

                elif level_return == 'victory':
                    Victory(self.window).run()

            elif menu_return == MENU_OPTION[1]:
                About(self.window).run()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()

            else:
                pygame.quit()
                sys.exit()
