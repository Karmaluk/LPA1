#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import ENEMY_SPAWN_INTERVAL, BOSS_SPAWN_TIME, COLOR_PURPLE_SELECTED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.player = Player('Player', (0, 450))
        self.window = window
        self.game_mode = game_mode
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.spawn_timer = 0
        self.frame_count = 0
        self.boss_spawned = False

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        while True:
            clock.tick(30)
            self.frame_count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.frame_count >= BOSS_SPAWN_TIME and not self.boss_spawned:
                self.entity_list.append(EntityFactory.get_entity('EnemyBoss'))
                pygame.mixer_music.load(f'./asset/Boss.wav')
                pygame.mixer_music.set_volume(0.3)
                pygame.mixer_music.play(-1)
                self.boss_spawned = True
            if not self.boss_spawned:
                self.spawn_timer += 1
                if self.spawn_timer >= ENEMY_SPAWN_INTERVAL:
                    enemy_type = random.choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(EntityFactory.get_entity(enemy_type))
                    self.spawn_timer = 0
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.update()
            self.entity_list = [
                ent for ent in self.entity_list
                if not (isinstance(ent, Entity) and ent.rect.right < 0)
            ]
            if not self.boss_spawned:
                seconds_left = max(0, (BOSS_SPAWN_TIME - self.frame_count) // 30)
                self.level_text(25, f'Boss in: {seconds_left}s',
                                text_color=COLOR_PURPLE_SELECTED, text_pos=(800, 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='./asset/DarkForestFont.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
