#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.velocity_y = 0
        self.gravity = 1
        self.jump_power = -15
        self.is_on_ground = True
        self.health = ENTITY_HEALTH.get(name, 100)

    @abstractmethod
    def move(self):
        pass

    def update(self):
        pass
