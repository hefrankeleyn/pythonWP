import sys,pygame
from settings import Settings
from ship import Ship 
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #init a screen
    pygame.init()
    #set screen width and height
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #Create a game_stats
    stats=GameStats(ai_settings)
    
    score_board=Scoreboard(ai_settings,screen,stats)
    
    #Create a ship
    ship=Ship(ai_settings,screen)
    
    #Create a Group of alien
    aliens=Group()
    
    #Create a Group that store the bullet
    bullets=Group()
    
    #Create a group of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #Create Plag button
    play_button=Button(ai_settings,screen,'Play')
    
    #begin game main loop
    while True:
        gf.check_events(ai_settings,screen,stats,score_board,play_button,ship,
            aliens,bullets)
        if stats.game_active:
            ship.update()
            
            gf.update_bullets(ai_settings,screen,stats,score_board,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,score_board,ship,aliens,bullets)
            #print(len(bullets))
        gf.update_screen(ai_settings,screen,stats,score_board,ship,aliens,
            bullets,play_button)
        
        

run_game()
        
