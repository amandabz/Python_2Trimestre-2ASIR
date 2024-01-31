# Amanda Benítez Hidalgo
import pygame
import sys
import random

# initialize pygame
pygame.init()

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PINK = (255, 182, 193)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# screen configuration
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("arkanoid with colorful blocks")

# font
font = pygame.font.Font(None, 36)

# ball configuration
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 35, 35)
ball_speed = [8, 8]

# paddle configuration
paddle = pygame.Rect(width // 2 - 60, height - 20, 120, 10)
paddle_speed = 10

# blocks configuration
block_width, block_height = 50, 20
blocks = []
colors = [BLUE, RED, GREEN, YELLOW, PINK, PURPLE, ORANGE]

for row in range(5):
    for col in range(width // block_width):
        block = pygame.Rect(col * block_width, row * block_height + 50, block_width, block_height)
        color = random.choice(colors)
        blocks.append((block, color))

# score
score = 0
game_over = False
win = False

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over and not win:
        # paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-paddle_speed, 0)
        if keys[pygame.K_RIGHT] and paddle.right < width:
            paddle.move_ip(paddle_speed, 0)

        # ball movement
        ball.move_ip(ball_speed)

        # ball bounce on the edges
        if ball.left < 0 or ball.right > width:
            ball_speed[0] = -ball_speed[0]
        if ball.top < 0:
            ball_speed[1] = -ball_speed[1]

        # ball bounce on the paddle
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]

        # check for collisions with blocks
        for block, color in blocks[:]:
            if ball.colliderect(block):
                ball_speed[1] = -ball_speed[1]
                blocks.remove((block, color))
                score += 1

        # check for win condition
        if not blocks:
            win = True

        # check for game over condition
        if ball.bottom > height:
            game_over = True

        # draw on the screen
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        for block, color in blocks:
            pygame.draw.rect(screen, color, block)
        score_text = font.render(f"Score: {score}", True, BLUE)
        screen.blit(score_text, (10, 10))

    elif win:
        win_text = font.render("You Win! Press R to Play Again", True, BLUE)
        screen.blit(win_text, (width // 4, height // 2))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            blocks = []
            for row in range(5):
                for col in range(width // block_width):
                    block = pygame.Rect(col * block_width, row * block_height + 50, block_width, block_height)
                    color = random.choice(colors)
                    blocks.append((block, color))
            score = 0
            ball.x = width // 2 - 15
            ball.y = height // 2 - 15
            game_over = False
            win = False

    elif game_over:
        game_over_text = font.render("Game Over! Press R to Play Again", True, WHITE)
        screen.blit(game_over_text, (width // 4, height // 2))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            blocks = []
            for row in range(5):
                for col in range(width // block_width):
                    block = pygame.Rect(col * block_width, row * block_height + 50, block_width, block_height)
                    color = random.choice(colors)
                    blocks.append((block, color))
            score = 0
            ball.x = width // 2 - 15
            ball.y = height // 2 - 15
            game_over = False
            win = False

    pygame.display.flip()
    pygame.time.Clock().tick(30)
