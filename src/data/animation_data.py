from src.settings import *

FROG_DATA = {
    NAME: PLAYER,
    ANIMATIONS: [
        {
            NAME: IDLE,
            FRAMES: 4,
        },
        {
            NAME: LICK,
            FRAMES: 4,
        },
        {
            NAME: HURT,
            FRAMES: 2,
        },
    ]
}

FRIEND_DATA = {
    NAME: FRIEND_FROG,
    ANIMATIONS: [
        {
            NAME: IDLE,
            FRAMES: 4,
        },
    ]
}

FLY_DATA = {
    NAME: ENEMY_FLY,
    ANIMATIONS: [
        {
            NAME: IDLE,
            FRAMES: 4,
        },
    ]
}

BIRD_DATA = {
    NAME: ENEMY_BIRD,
    ANIMATIONS: [
        {
            NAME: IDLE,
            FRAMES: 6,
        },
    ]
}

HEART_DATA = {
    NAME: UI_HEART,
    ANIMATIONS: [
        {
            NAME: IDLE,
            FRAMES: 1,
        },
        {
            NAME: EMPTY,
            FRAMES: 1,
        },
    ]
}