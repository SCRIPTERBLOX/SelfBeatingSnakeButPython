import pygame
import random
import numpy as np

import snake_ai

defSnake = [
    [16, 16],
    [16, 17],
    [16, 18],
    [16, 19],
    [16, 20]
]

gameSizeX = 32
gameSizeY = 30

snake = defSnake

snakeDir = "W"
nextDir = "W"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((10+gameSizeX*25+200, 10+gameSizeY*25))
clock = pygame.time.Clock()
running = True

food = ["x", "x"]
growFor = (gameSizeY-1)*(gameSizeX-1)/2

def get_pos_x_y(): return [random.randint(0, gameSizeX-1), random.randint(0, gameSizeY-1)]

def get_food_pos():
    new_food = get_pos_x_y()

    if new_food in snake:
        return get_food_pos()
    else:
        return new_food

def integer_to_rgb(value, max_value):
    # Normalize the value to a range of 0 to 1
    normalized_value = value / max_value

    # Map the normalized value to the hue (0 to 1), starting at 120 degrees (green)
    hue = (normalized_value * 360 + 120) % 360  # Offset start by 120 degrees

    # Convert HSV to RGB
    c = 1  # Full saturation and value (brightness)
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = 0  # Offset to bring RGB to 0-1 range

    if 0 <= hue < 60:
        r, g, b = c, x, m
    elif 60 <= hue < 120:
        r, g, b = x, c, m
    elif 120 <= hue < 180:
        r, g, b = m, c, x
    elif 180 <= hue < 240:
        r, g, b = m, x, c
    elif 240 <= hue < 300:
        r, g, b = x, m, c
    else:
        r, g, b = c, m, x

    # Scale to 0-255
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)

    return r, g, b

gradient = np.zeros((50, gameSizeX*gameSizeY, 3), dtype=np.uint8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    nextDir = snake_ai.bot_do(snake, gameSizeY, nextDir, food, gameSizeX)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((50, 50, 50))

    if not len(snake) == (gameSizeX-1)*(gameSizeY-1):
        if food == ["x", "x"]: food = get_food_pos()

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200, 0, gameSizeX*25+10, gameSizeY*25+10))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(205, 5, gameSizeX*25, gameSizeY*25))

    if not food == ["x", "x"]:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food[0]*25+205, food[1]*25+5, 25, 25))

    head = snake[0].copy()
    newHead = head.copy()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not snakeDir == "S":
            nextDir = "W"
    if keys[pygame.K_s]:
        if not snakeDir == "W":
            nextDir = "S"
    if keys[pygame.K_a]:
        if not snakeDir == "D":
            nextDir = "A"
    if keys[pygame.K_d]:
        if not snakeDir == "A":
            nextDir = "D"

    snakeDir = nextDir

    if snakeDir == "W":
        newHead[1] -= 1
    if snakeDir == "S":
        newHead[1] += 1
    if snakeDir == "A":
        newHead[0] -= 1
    if snakeDir == "D":
        newHead[0] += 1

    if newHead == food:
        newSnake = [newHead]
        for i in range(len(snake)): newSnake.append(snake[i])
        food = ["x", "x"]
    else:
        if growFor > 0:
            newSnake = [newHead]
            for i in range(len(snake)): newSnake.append(snake[i])
            growFor -= 1
        else:
            newSnake = [newHead]
            for i in range(len(snake)-1): newSnake.append(snake[i])

    for i in range(len(newSnake)):
        if not i == 0:
            if newHead == newSnake[i]: newSnake = defSnake

    if newHead[0] > gameSizeX-1 or newHead[0] < 0 or newHead[1] > gameSizeY-1 or newHead[1] < 0:
        newSnake = defSnake
        snakeDir = "W"
        nextDir = "W"

    snake = newSnake

    #render the snake
    for i in range(len(snake)):
        pygame.draw.rect(
            screen,
            (integer_to_rgb(i, gameSizeX*gameSizeY)),
            pygame.Rect(205+(snake[i][0]*25), 5+(snake[i][1]*25), 25, 25)
        )

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(1000) / 1000

pygame.quit()