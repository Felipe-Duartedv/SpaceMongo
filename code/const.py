import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                     'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                    'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

SPAWN_TIME = 4000


WIN_WIDTH = 576
WIN_HEIGHT = 324