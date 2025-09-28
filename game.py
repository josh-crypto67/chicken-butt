# chicken-butt
import pygame
import sys
import math

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Ball Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Ball settings
BALL_RADIUS = 10
ball_a_pos = [100, HEIGHT // 2]
ball_b_pos = [100, HEIGHT // 2]

# Path
path = []
drawing = False
follow_index = 0
following = False
speed = 3  # pixels per frame

clock = pygame.time.Clock()

def move_towards(pos, target, speed):
    dx, dy = target[0] - pos[0], target[1] - pos[1]
    distance = math.hypot(dx, dy)
    if distance < speed or distance == 0:
        return target
    else:
        return [pos[0] + speed * dx / distance, pos[1] + speed * dy / distance]

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start drawing path when mouse is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and not following:
            drawing = True
            path = []
            ball_a_pos = list(pygame.mouse.get_pos())
            path.append(ball_a_pos[:])

        # Stop drawing when mouse released
        if event.type == pygame.MOUSEBUTTONUP and not following:
            drawing = False

        # Start following the path
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and path:
                following = True
                follow_index = 0
                ball_b_pos = path[0][:]

    # Draw and record path
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if not path or math.hypot(mouse_pos[0] - path[-1][0], mouse_pos[1] - path[-1][1]) > 5:
            path.append(mouse_pos[:])
        ball_a_pos = mouse_pos[:]

    # Ball B follows the path
    if following and follow_index < len(path):
        ball_b_pos = move_towards(ball_b_pos, path[follow_index], speed)
        if math.hypot(ball_b_pos[0] - path[follow_index][0], ball_b_pos[1] - path[follow_index][1]) < 2:
            follow_index += 1

    # Draw path
    if len(path) > 1:
        pygame.draw.lines(screen, BLACK, False, path, 2)

    # Draw balls
    pygame.draw.circle(screen, RED, (int(ball_a_pos[0]), int(ball_a_pos[1])), BALL_RADIUS)
    pygame.draw.circle(screen, BLUE, (int(ball_b_pos[0]), int(ball_b_pos[1])), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)
