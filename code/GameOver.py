#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface
from code.Const import COLOR_RED, COLOR_PURPLE_DARK, WIN_WIDTH, WIN_HEIGHT, COLOR_BLACK


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOver.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        pygame.mixer.music.load('./asset/GameOver.wav')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.screen_text(200, 'Game Over', COLOR_PURPLE_DARK, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 150))
            self.screen_text(50, 'You have fallen in the Dark Forest',
                             COLOR_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))
            self.screen_text(50, 'Press ENTER to return to menu',
                             COLOR_BLACK, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 250))
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