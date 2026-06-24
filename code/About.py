#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface
from code.Const import COLOR_WHITE, COLOR_PURPLE, COLOR_PURPLE_DARK, COLOR_PURPLE_SELECTED, WIN_WIDTH


class About:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png').convert_alpha()  # reuse menu bg
        self.rect = self.surf.get_rect()

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.screen_text(100, 'Dark Forest', COLOR_PURPLE, (WIN_WIDTH // 2, 80))
            self.screen_text(80, 'About', COLOR_PURPLE_SELECTED, (WIN_WIDTH // 2, 150))
            self.screen_text(30, 'A side-scrolling survival game', COLOR_PURPLE, (WIN_WIDTH // 2, 370))
            self.screen_text(30, 'built with Python and Pygame', COLOR_PURPLE, (WIN_WIDTH // 2, 390))
            self.screen_text(30, 'Survive enemy waves and defeat the boss!', COLOR_PURPLE, (WIN_WIDTH // 2, 410))
            self.screen_text(30, 'Developed by: Vinicius Karmaluk', COLOR_PURPLE, (WIN_WIDTH // 2, 450))
            self.screen_text(35, 'Press ENTER to go back', COLOR_PURPLE, (WIN_WIDTH // 2, 510))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'menu'

    def screen_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font('./asset/DarkForestFont.ttf', text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
