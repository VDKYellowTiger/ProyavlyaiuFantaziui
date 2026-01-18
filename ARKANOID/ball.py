import pygame
from settings import WHITE, BALL_RADIUS, BALL_SPEED_X, BALL_SPEED_Y

class Ball:
    def __init__(self, screen_width, screen_height):
        self.rect = pygame.Rect(
            screen_width // 2 - BALL_RADIUS,
            screen_height // 2 - BALL_RADIUS,
            BALL_RADIUS*2,
            BALL_RADIUS*2
        )
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def check_wall_collision(self, screen_width, screen_height):
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= screen_height:
            return True  # Мяч упал, игра окончена
        return False

    def check_paddle_collision(self, paddle_rect):
        if self.rect.colliderect(paddle_rect):
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)