#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_FLOOR
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (0, ENTITY_FLOOR))
