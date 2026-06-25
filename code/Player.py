#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_FLOOR, PLAYER_SHOT_COOLDOWN
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_cooldown = 0
        self.pending_shot = False

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_UP] and self.is_on_ground:
            self.velocity_y = self.jump_power
            self.is_on_ground = False
        self.pending_shot = False
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if pressed_keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.pending_shot = True
            self.shoot_cooldown = PLAYER_SHOT_COOLDOWN

    def update(self):
        if not self.is_on_ground:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            if self.rect.y >= ENTITY_FLOOR:
                self.rect.y = ENTITY_FLOOR
                self.velocity_y = 0
                self.is_on_ground = True
