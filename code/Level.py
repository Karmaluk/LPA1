#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import (ENEMY_SPAWN_INTERVAL, BOSS_SPAWN_TIME,
                        WIN_WIDTH, ENTITY_DAMAGE, COLOR_WHITE, COLOR_RED, COLOR_PURPLE_SELECTED)
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.PlayerShot import PlayerShot


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.game_mode = game_mode
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.spawn_timer = 0
        self.frame_count = 0
        self.boss_spawned = False
        self.heart_surf = pygame.image.load('./asset/HeartFull.png').convert_alpha()

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
                pygame.mixer.music.load(f'./asset/Boss.wav')
                pygame.mixer_music.set_volume(0.3)
                pygame.mixer_music.play(-1)
                self.boss_spawned = True
            if not self.boss_spawned:
                self.spawn_timer += 1
                if self.spawn_timer >= ENEMY_SPAWN_INTERVAL:
                    enemy_type = random.choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(EntityFactory.get_entity(enemy_type))
                    self.spawn_timer = 0
            shots_to_add: list[Entity] = []
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.update()

                if isinstance(ent, Player) and ent.pending_shot:
                    shot_pos = (ent.rect.right, ent.rect.centery)
                    shots_to_add.append(EntityFactory.get_entity('PlayerShot', shot_pos))

                if isinstance(ent, Enemy) and ent.pending_shot:
                    shot_pos = (ent.rect.left, ent.rect.centery)
                    shots_to_add.append(EntityFactory.get_entity('EnemyShot', shot_pos))

            self.entity_list.extend(shots_to_add)

            self._handle_collisions()

            self.entity_list = [
                ent for ent in self.entity_list
                if ent.health > 0 and ent.rect.right > 0
            ]

            self._draw_hud()

            player = next((e for e in self.entity_list if isinstance(e, Player)), None)
            if player is None or player.health <= 0:
                pygame.mixer.music.stop()
                return 'game_over'

            if self.boss_spawned:
                boss = next((e for e in self.entity_list
                             if isinstance(e, Enemy) and 'Boss' in e.name), None)
                if boss is None:
                    pygame.mixer.music.stop()
                    return 'victory'

            pygame.display.flip()

    def _handle_collisions(self):
        players = [e for e in self.entity_list if isinstance(e, Player)]
        enemies = [e for e in self.entity_list if isinstance(e, Enemy)]
        player_shots = [e for e in self.entity_list if isinstance(e, PlayerShot)]
        enemy_shots = [e for e in self.entity_list if isinstance(e, EnemyShot)]

        for shot in player_shots:
            for enemy in enemies:
                if shot.rect.colliderect(enemy.rect):
                    enemy.health -= ENTITY_DAMAGE['PlayerShot']
                    shot.health = 0
                    break

        for shot in enemy_shots:
            for player in players:
                if shot.rect.colliderect(player.rect):
                    player.health -= ENTITY_DAMAGE['EnemyShot']
                    shot.health = 0
                    break

        for enemy in enemies:
            for player in players:
                if enemy.rect.colliderect(player.rect):
                    player.health -= ENTITY_DAMAGE[enemy.name]
                    enemy.health = 0

    def _draw_hud(self):
        player = next((e for e in self.entity_list if isinstance(e, Player)), None)

        if player:
            max_hearts = 3
            hearts = max(0, round(player.health / (100 / max_hearts)))
            for i in range(max_hearts):
                if i < hearts:
                    self.window.blit(self.heart_surf, (10 + i * 38, 10))
                else:
                    empty = self.heart_surf.copy()
                    empty.set_alpha(60)
                    self.window.blit(empty, (10 + i * 38, 10))

            self.level_text(20, f'HP: {max(0, player.health)}', COLOR_PURPLE_SELECTED, (10, 40))

        if not self.boss_spawned:
            seconds_left = max(0, (BOSS_SPAWN_TIME - self.frame_count) // 30)
            self.level_text(20, f'Boss in: {seconds_left}s', COLOR_PURPLE_SELECTED, (WIN_WIDTH - 160, 10))
        else:

            boss = next((e for e in self.entity_list if isinstance(e, Enemy)
                         and 'Boss' in e.name), None)
            if boss:
                bar_x, bar_y, bar_w, bar_h = WIN_WIDTH // 4, 20, WIN_WIDTH // 2, 16
                ratio = max(0, boss.health / 100)
                pygame.draw.rect(self.window, (80, 0, 0), (bar_x, bar_y, bar_w, bar_h))
                pygame.draw.rect(self.window, COLOR_RED, (bar_x, bar_y, int(bar_w * ratio), bar_h))
                pygame.draw.rect(self.window, COLOR_WHITE, (bar_x, bar_y, bar_w, bar_h), 2)
                self.level_text(30, 'BOSS', COLOR_PURPLE_SELECTED, (bar_x + bar_w // 2 - 16, bar_y - 18))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='./asset/DarkForestFont.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
