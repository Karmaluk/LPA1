#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2 - 30))
                # list_idle = []
                # for i in range(1):
                #     list_idle.append(Background(f'Player_Idle_R{i}', (300, 300)))
                # return list_idle
