import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """init the ship"""
        self.screen=screen
        self.ai_settings=ai_settings
        
        #download the ship and fetch the around of the ship
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #make the ship on the botton and center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.center=float(self.rect.centerx)
        
        #the flag of move 
        self.moving_right=False
        self.moving_left=False
    
    def blitme(self):
        """draw the ship on the point"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            #self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            #self.rect.centerx-=1
            self.center-=self.ai_settings.ship_speed_factor
        
        #update self.rect.centerx flow self.center
        self.rect.centerx=self.center
    
    def center_ship(self):
        self.center=self.screen_rect.centerx
