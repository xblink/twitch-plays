
import pygame
from pygame.locals import *
import lib.graph

class GUI:
    def __init__(self, bot):
        self.bot = bot
        self.stats = self.bot.stats
        
        pygame.init()
        self.displaySurface = pygame.display.set_mode((450,800), pygame.HWSURFACE)
        
    def run(self):
        self.update()
        self.draw()
        
    def update(self):
        pass
    
    def draw(self):
        pass