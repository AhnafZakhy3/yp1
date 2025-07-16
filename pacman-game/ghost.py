import pygame
import random
from config import *

class Ghost:
    def __init__(self, name, maze):
        self.name = name
        self.maze = maze
        self.position = list(GHOST_START_POS[self.name])
        self.direction = (0, 0)
        self.speed = GHOST_SPEED
        self.color = self.get_color()
        self.radius = TILE_SIZE // 3
        self.is_frightened = False
        self.frightened_timer = 0
        
        # Create rect for collision detection
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.update_rect()
    
    def get_color(self):
        colors = {
            'blinky': RED,
            'pinky': PINK,
            'inky': CYAN,
            'clyde': (255, 184, 82)  # Orange
        }
        return colors[self.name]
    
    def update(self, player):
        if self.is_frightened:
            self.frightened_timer -= 1
            if self.frightened_timer <= 0:
                self.is_frightened = False
        
        self.choose_direction(player)
        self.move()
    
    def draw(self, screen):
        # Draw ghost
        center = (self.rect.centerx, self.rect.centery)
        if self.is_frightened:
            color = BLUE
        else:
            color = self.color
        
        pygame.draw.circle(screen, color, center, self.radius)
        # Draw eyes
        eye_offset = self.radius // 3
        pygame.draw.circle(screen, WHITE, (center[0] - eye_offset, center[1] - eye_offset), self.radius // 4)
        pygame.draw.circle(screen, WHITE, (center[0] + eye_offset, center[1] - eye_offset), self.radius // 4)
    
    def choose_direction(self, player):
        # Basic AI for ghost movement
        if self.is_frightened:
            self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        else:
            # Chase player based on ghost type
            target = self.get_target(player)
            directions = self.get_possible_directions()
            best_dir = None
            min_distance = float('inf')
            
            for dir in directions:
                new_pos = [self.position[0] + dir[0], self.position[1] + dir[1]]
                distance = ((new_pos[0] - target[0]) ** 2 + (new_pos[1] - target[1]) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    best_dir = dir
            
            self.direction = best_dir
    
    def get_target(self, player):
        # Different targeting behavior for each ghost
        if self.name == 'blinky':
            return player.position
        elif self.name == 'pinky':
            return [player.position[0] + 4 * player.direction[0],
                   player.position[1] + 4 * player.direction[1]]
        elif self.name == 'inky':
            blinky_pos = [self.position[0] + 2 * (player.position[0] - self.position[0]),
                         self.position[1] + 2 * (player.position[1] - self.position[1])]
            return blinky_pos
        elif self.name == 'clyde':
            distance = ((self.position[0] - player.position[0]) ** 2 +
                       (self.position[1] - player.position[1]) ** 2) ** 0.5
            if distance > 8:
                return player.position
            else:
                return GHOST_START_POS[self.name]
    
    def get_possible_directions(self):
        directions = []
        for dir in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if dir != (-self.direction[0], -self.direction[1]):  # Can't reverse direction
                test_rect = self.rect.move(dir[0] * self.speed, dir[1] * self.speed)
                if not self.maze.check_wall_collision(test_rect):
                    directions.append(dir)
        return directions
    
    def move(self):
        if self.can_move(self.direction):
            self.position[0] += self.direction[0] * self.speed
            self.position[1] += self.direction[1] * self.speed
            self.update_rect()
    
    def can_move(self, direction):
        test_rect = self.rect.move(direction[0] * self.speed, direction[1] * self.speed)
        return not self.maze.check_wall_collision(test_rect)
    
    def set_frightened(self):
        self.is_frightened = True
        self.frightened_timer = FPS * 10  # 10 seconds
    
    def respawn(self):
        self.position = list(GHOST_START_POS[self.name])
        self.direction = (0, 0)
        self.is_frightened = False
        self.update_rect()
    
    def update_rect(self):
        self.rect.center = (self.position[0] * TILE_SIZE + TILE_SIZE // 2,
                          self.position[1] * TILE_SIZE + TILE_SIZE // 2)
