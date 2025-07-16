import pygame
from config import *

class Maze:
    def __init__(self):
        self.walls = self.create_walls()
        self.pellets = self.create_pellets()
        self.power_pellets = self.create_power_pellets()
    
    def create_walls(self):
        # Classic Pacman maze layout
        walls = [
            # Horizontal walls
            (0, 0, MAZE_WIDTH, 1),
            (0, MAZE_HEIGHT - 1, MAZE_WIDTH, 1),
            # Vertical walls
            (0, 0, 1, MAZE_HEIGHT),
            (MAZE_WIDTH - 1, 0, 1, MAZE_HEIGHT),
            # Inner walls
            (2, 2, 5, 1),
            (8, 2, 5, 1),
            (15, 2, 5, 1),
            (21, 2, 5, 1),
            # Add more walls as needed...
        ]
        return [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, w * TILE_SIZE, h * TILE_SIZE) 
               for x, y, w, h in walls]
    
    def create_pellets(self):
        pellets = []
        for x in range(1, MAZE_WIDTH - 1):
            for y in range(1, MAZE_HEIGHT - 1):
                if not self.check_wall_collision(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, 1, 1)):
                    pellets.append(Pellet(x, y))
        return pellets
    
    def create_power_pellets(self):
        power_pellets = [
            (1, 1),
            (MAZE_WIDTH - 2, 1),
            (1, MAZE_HEIGHT - 2),
            (MAZE_WIDTH - 2, MAZE_HEIGHT - 2)
        ]
        return [Pellet(x, y, is_power=True) for x, y in power_pellets]
    
    def check_wall_collision(self, rect):
        for wall in self.walls:
            if rect.colliderect(wall):
                return True
        return False
    
    def check_pellet_collision(self, rect):
        for pellet in self.pellets:
            if rect.colliderect(pellet.rect):
                return pellet
        for pellet in self.power_pellets:
            if rect.colliderect(pellet.rect):
                return pellet
        return None
    
    def remove_pellet(self, pellet):
        if pellet in self.pellets:
            self.pellets.remove(pellet)
        elif pellet in self.power_pellets:
            self.power_pellets.remove(pellet)
    
    def draw(self, screen):
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)
        
        # Draw pellets
        for pellet in self.pellets:
            pellet.draw(screen)
        for pellet in self.power_pellets:
            pellet.draw(screen)

class Pellet:
    def __init__(self, x, y, is_power=False):
        self.position = (x, y)
        self.is_power = is_power
        self.radius = TILE_SIZE // 8 if not is_power else TILE_SIZE // 4
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.update_rect()
    
    def draw(self, screen):
        center = (self.rect.centerx, self.rect.centery)
        pygame.draw.circle(screen, WHITE, center, self.radius)
    
    def update_rect(self):
        self.rect.center = (self.position[0] * TILE_SIZE + TILE_SIZE // 2,
                          self.position[1] * TILE_SIZE + TILE_SIZE // 2)
