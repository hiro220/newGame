from character.enemy.exsample_enemy import EnemySample
from character.player import PlayerSample
from objects.wall_object import WallObject, MovingFloor

_object_list = \
[
    EnemySample,
    PlayerSample,
    WallObject,
    MovingFloor
]

GameObject = {}
for _id, _object in enumerate(_object_list):
    GameObject[str(_id)] = _object