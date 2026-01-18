import pygame
from settings import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, BLUE

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.rect = pygame.Rect(
            screen_width // 2 - PADDLE_WIDTH // 2,
            screen_height - 40,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )
        self.speed = PADDLE_SPEED

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.right += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)