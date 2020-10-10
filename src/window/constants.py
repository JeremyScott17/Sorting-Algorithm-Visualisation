import pygame


# window information
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
GRAPH_WIDTH, GRAPH_HEIGHT = (3 * WINDOW_WIDTH) / 4, WINDOW_HEIGHT
CONTROL_WIDTH, CONTROL_HEIGHT = WINDOW_WIDTH / 4, WINDOW_HEIGHT

# button information
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 100
GEN_BTN_X = SORT_BTN_X = RESET_BTN_X = GRAPH_WIDTH + (CONTROL_WIDTH / 2) - (BUTTON_WIDTH / 2)
GEN_BTN_Y = 100
SORT_BTN_Y = 250
RESET_BTN_Y = 400

# colours in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
DARK_GRAY = (64, 64, 64)
DARKER_GRAY = (32, 32, 32)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)