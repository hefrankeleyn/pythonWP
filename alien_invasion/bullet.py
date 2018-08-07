import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manager the bullet"""
    def __init__(self,ai_settings,screen,ship):
        """Create a bullet"""
        super().__init__()
        self.screen=screen
        
        #Create Rect on (0,0),and set right pointion
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        #store bullet postition
        self.y=float(self.rect.y)
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    
    def update(self):
        """move the bullet up"""
        self.y-=self.speed_factor
        #update bullet's rect position
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
