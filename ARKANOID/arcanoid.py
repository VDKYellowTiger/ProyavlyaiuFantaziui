import pygame
import sys
from settings import WIDTH, HEIGHT, BRICK_ROWS, BRICK_COLS
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")
clock = pygame.time.Clock()

# Создание объектов
paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)

# Создание кирпичей
brick_width = WIDTH // BRICK_COLS
bricks = [Brick(col * brick_width, row * 30 + 50, brick_width - 5, 30 - 5)
          for row in range(BRICK_ROWS) for col in range(BRICK_COLS)]

# Основной цикл
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle.move(keys, WIDTH)
    ball.move()

    if ball.check_wall_collision(WIDTH, HEIGHT):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    ball.check_paddle_collision(paddle.rect)

    # Проверка столкновения с кирпичами
    hit_index = ball.rect.collidelist([b.rect for b in bricks])
    if hit_index != -1:
        bricks.pop(hit_index)
        ball.speed_y *= -1

    # Отрисовка
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    if not bricks:
        print("You Win!")
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)