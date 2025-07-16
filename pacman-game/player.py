import pygame
from config import *

class Player:
    def __init__(self, maze):
        self.maze = maze
        self.position = list(PLAYER_START_POS)
        self.direction = (0, 0)
        self.next_direction = (0, 0)
        self.speed = PLAYER_SPEED
        self.radius = TILE_SIZE // 3
        self.mouth_angle = 0
        self.mouth_speed = 5
        
        # Create rect for collision detection
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.update_rect()
    
    def update(self):
        # Handle movement
        self.handle_input()
        self.move()
        self.animate_mouth()
    
    def draw(self, screen):
        # Draw Pacman
        center = (self.rect.centerx, self.rect.centery)
        start_angle = self.mouth_angle
        end_angle = 360 - self.mouth_angle
        
        pygame.draw.circle(screen, YELLOW, center, self.radius)
        pygame.draw.polygon(screen, BLACK, [
            center,
            (center[0] + self.radius * pygame.math.Vector2().from_polar((1, start_angle))[0],
             center[1] + self.radius * pygame.math.Vector2().from_polar((1, start_angle))[1]),
            (center[0] + self.radius * pygame.math.Vector2().from_polar((1, end_angle))[0],
             center[1] + self.radius * pygame.math.Vector2().from_polar((1, end_angle))[1])
        ])
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.next_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            self.next_direction = (0, 1)
        elif keys[pygame.K_LEFT]:
            self.next_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.next_direction = (1, 0)
    
    def move(self):
        # Check if next direction is valid
        if self.can_move(self.next_direction):
            self.direction = self.next_direction
        
        # Move in current direction if possible
        if self.can_move(self.direction):
            self.position[0] += self.direction[0] * self.speed
            self.position[1] += self.direction[1] * self.speed
            self.update_rect()
    
    def can_move(self, direction):
        # Check if movement in given direction is possible
        test_rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)
        return not self.maze.check_wall_collision(test_rect)
    
    def animate_mouth(self):
        self.mouth_angle += self.mouth_speed
        if self.mouth_angle > 45 or self.mouth_angle < 0:
            self.mouth_speed *= -1
    
    def update_rect(self):
        self.rect.center = (self.position[0] * TILE_SIZE + TILE_SIZE // 2,
                          self.position[1] * TILE_SIZE + TILE_SIZE // 2)
    
    def respawn(self):
        self.position = list(PLAYER_START_POS)
        self.direction = (0, 0)
        self.next_direction = (0, 0)
        self.update_rect()
