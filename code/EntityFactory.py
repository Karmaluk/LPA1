#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Enemy import Enemy
from code.Background import Background
from code.Const import WIN_WIDTH, ENTITY_FLOOR
from code.Player import Player
from code.PlayerShot import PlayerShot


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
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, ENTITY_FLOOR))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, ENTITY_FLOOR))
            case 'EnemyBoss':
                return Enemy('EnemyBoss', (WIN_WIDTH + 10, ENTITY_FLOOR - 65))
            case 'PlayerShot':
                return PlayerShot('PlayerShot', position)
            case 'EnemyShot':
                return EnemyShot('EnemyShot', position)
