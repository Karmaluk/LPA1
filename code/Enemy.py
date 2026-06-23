#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_every = 60 if 'Boss' not in name else 40
        self.shoot_timer = random.randint(0, self.shoot_every)
        self.pending_shot = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def update(self):
        self.pending_shot = False
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_every:
            self.pending_shot = True
            self.shoot_timer = 0
