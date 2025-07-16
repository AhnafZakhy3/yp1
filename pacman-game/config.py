# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 660

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 184, 255)
CYAN = (0, 255, 255)

# Game settings
FPS = 60
TILE_SIZE = 30
PLAYER_SPEED = 2
GHOST_SPEED = 1.8
FRIGHTENED_SPEED = 1.5

# Maze settings
MAZE_WIDTH = 28
MAZE_HEIGHT = 31

# Player settings
PLAYER_START_POS = (14, 23)

# Ghost settings
GHOST_START_POS = {
    'blinky': (14, 11),
    'pinky': (14, 14),
    'inky': (12, 14),
    'clyde': (16, 14)
}

# Scoring
PELLET_SCORE = 10
POWER_PELLET_SCORE = 50
GHOST_SCORE = 200

# Game states
PLAYING = 0
PAUSED = 1
GAME_OVER = 2
