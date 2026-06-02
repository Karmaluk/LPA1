#!/usr/bin/python
# -*- coding: utf-8 -*-


from code.Menu import Menu

import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         quit()
