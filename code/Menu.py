#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_PURPLE_DARK, MENU_OPTION, COLOR_PURPLE_SELECTED, COLOR_PURPLE, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.wav')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(270, "Dark Forest", text_color=COLOR_PURPLE,
                           text_center_pos=(500, 120))
            self.menu_text(30, 'Arrow keys to move  |  UP to jump', COLOR_BLACK, (180, 470))
            self.menu_text(30, 'SPACE to shoot  |  ENTER to select', COLOR_BLACK, (180, 500))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(60, MENU_OPTION[i], COLOR_PURPLE_SELECTED,
                                   (500, 380 + 50 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_PURPLE_DARK,
                                   (500, 380 + 50 * i))
            pygame.display.flip()

            for event in pygame.event.get():  # CHECK FOR EVERY EVENT
                if event.type == pygame.QUIT:
                    pygame.quit()  # CLOSE WINDOW
                    quit()  # END PYGAME
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # RETURN KEY PRESSED
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/DarkForestFont.ttf', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
