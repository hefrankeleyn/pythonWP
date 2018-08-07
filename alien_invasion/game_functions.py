import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def get_number_aliens_x(ai_settings,alien_width):
    """Create a group of aliens"""
    #Create a alien for calculate nums of one col
    #the distance of one alien to alien is one alien of width
    available_space_x=ai_settings.screen_width-2*alien_width
    number_alien_x=int(available_space_x/(2*alien_width))
    return number_alien_x

def get_number_aliens_y(ai_settings,ship_height,alien_height):
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows


#Create alien
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #Create a alien and in the col
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    #get num of a col
    number_alien_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_aliens_y(ai_settings,ship.rect.height,
        alien.rect.height)


    #Create the first col alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """response the KEYDOWN"""
    if event.key==pygame.K_RIGHT:
        #move the ship to right 
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()
        
        
def fire_bullet(ai_settings,screen,ship,bullets):
    """Create one bullet"""
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    
def check_keyup_events(event,ship):
    """response the KEYUP"""
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    
    
def check_events(ai_settings,screen,stats,score_board,play_button,ship,aliens,bullets):
    #listen keyborad and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,score_board,play_button,
                ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,score_board,play_button,ship,
      aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        
        ai_settings.initialize_dynamic_settings()
        #hide 
        pygame.mouse.set_visible(False)
        #reset game
        stats.reset_stats()
        stats.game_active = True
        
        
        #reset photo
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_ships()
        
        #empty aliens and bullets
        aliens.empty()
        bullets.empty()
        ai_settings.increase_speed()
        #create a new group aliens
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
            
            
            
                
def update_screen(ai_settings,screen,stats,score_board,ship,aliens,bullets,play_button):
    #every time of loop reset the background
    screen.fill(ai_settings.bg_color) 
    
    #Dow all bullets on ship and alien blackboard
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    score_board.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
    #show laster screen
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,score_board,ship,aliens,bullets):
    # update bullet position
    bullets.update()
    #delete usered bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            print(bullet.rect.bottom)
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,score_board,ship,aliens,bullets)

def check_high_score(stats,score_board):
    if stats.score >stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()

def check_bullet_alien_collisions(ai_settings,screen,stats,score_board,ship,aliens,bullets):
    #search bullet if ticket alient
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level+=1
        score_board.prep_level()
        
        create_fleet(ai_settings,screen,ship,aliens)
        
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_high_score(stats,score_board)
        
def check_fleet_edges(ai_settings,aliens):
    """"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,screen,stats,score_board,ship,aliens,bullets):
    
    if stats.ships_left>0:
        stats.ships_left -= 1
        
        score_board.prep_ships()
        #empty alien and bullet
        aliens.empty()
        bullets.empty()
        
        #Create a group aliens
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        #sleep 
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
        
    
def update_aliens(ai_settings,screen,stats,score_board,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,score_board,ship,aliens,bullets)
    
    check_aliens_bottom(ai_settings,screen,stats,score_board,ship,aliens,
       bullets)
        
def check_aliens_bottom(ai_settings,screen,stats,score_board,ship,aliens,
     bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #deatil like ship_hit()
            ship_hit(ai_settings,screen,stats,score_board,ship,aliens,bullets)
            break
