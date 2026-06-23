#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key
from pygame import event

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_FLOOR
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_UP] and self.is_on_ground:
            self.velocity_y = self.jump_power
            self.is_on_ground = False

    def update(self):
        if not self.is_on_ground:
            self.velocity_y += self.gravity  # gravity pulls down each frame
            self.rect.y += self.velocity_y  # apply velocity to position
            if self.rect.y >= ENTITY_FLOOR:  # hit the floor?
                self.rect.y = ENTITY_FLOOR
                self.velocity_y = 0
                self.is_on_ground = True
