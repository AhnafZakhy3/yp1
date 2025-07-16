import pygame
from config import *
from player import Player
from ghost import Ghost
from maze import Maze

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = PLAYING
        self.score = 0
        self.lives = 3
        
        # Initialize game elements
        self.maze = Maze()
        self.player = Player(self.maze)
        self.ghosts = [
            Ghost('blinky', self.maze),
            Ghost('pinky', self.maze),
            Ghost('inky', self.maze),
            Ghost('clyde', self.maze)
        ]
    
    def update(self):
        if self.state == PLAYING:
            self.player.update()
            for ghost in self.ghosts:
                ghost.update(self.player)
            
            # Check for collisions
            self.check_collisions()
    
    def draw(self, screen):
        screen.fill(BLACK)
        self.maze.draw(screen)
        self.player.draw(screen)
        for ghost in self.ghosts:
            ghost.draw(screen)
        
        # Draw score and lives
        self.draw_hud(screen)
    
    def draw_hud(self, screen):
        font = pygame.font.SysFont('arial', 24)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
        screen.blit(score_text, (10, SCREEN_HEIGHT - 40))
        screen.blit(lives_text, (SCREEN_WIDTH - 120, SCREEN_HEIGHT - 40))
    
    def check_collisions(self):
        # Check player-ghost collisions
        for ghost in self.ghosts:
            if self.player.rect.colliderect(ghost.rect):
                if ghost.is_frightened:
                    self.score += GHOST_SCORE
                    ghost.respawn()
                else:
                    self.lose_life()
        
        # Check pellet collisions
        pellet = self.maze.check_pellet_collision(self.player.rect)
        if pellet:
            if pellet.is_power:
                self.score += POWER_PELLET_SCORE
                self.set_frightened_mode()
            else:
                self.score += PELLET_SCORE
            self.maze.remove_pellet(pellet)
    
    def set_frightened_mode(self):
        for ghost in self.ghosts:
            ghost.set_frightened()
    
    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.state = GAME_OVER
        else:
            self.player.respawn()
            for ghost in self.ghosts:
                ghost.respawn()
