#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= ENTITY_SPEED[self.name]
        pass
