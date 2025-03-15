#my first big project
import sys
from boss import Boss
from explosions import Explosion
from pathlib import Path
import json
from time import sleep
from meteor import Meteor
from random import randint
from stars import Star
from button import Button
from scoreboard import Scoreboard
import pygame
from bullet import Bullet, Boss_bullets
from alien import Alien
from setting import Settings
from game_stats import GameStats
from spaceship import Ship 
random_1 = randint(10,20)
random_2 = randint(10,20)
random_3 = randint(10,20)

class AlienInvasion:
    def __init__(self):
        pygame.init()#*initializing pygame library
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #! ALL THE SOUND EFFECTS
        pygame.mixer.music.load("sounds/layback.mp3") #! load of a playback sounds
        pygame.mixer.music.set_volume(0.05)#todo sets music volume
        pygame.mixer.music.play()#? play music
        self.wave = pygame.mixer.Sound("sounds/new_wavesf.mp3")
        self.wave.set_volume(0.1)
        self.shot = pygame.mixer.Sound("sounds/shot_sound_effect.mp3")
        self.shot.set_volume(0.14)
        self.Al_death = pygame.mixer.Sound("sounds/alien_death.mp3")
        self.Al_death.set_volume(0.1)
        self.lost_game = pygame.mixer.Sound("sounds/game_lost.mp3")
        self.lost_game.set_volume(0.1)
        self.hit = pygame.mixer.Sound("sounds/ship_damage.mp3") 
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_whith = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.font1 = pygame.font.SysFont("Arial", 60)
        self.loss_line = self.font1.render("you lose :(",True, (255,0,0))
        self.winner_line = self.font1.render("you win !!! (press q to restart)",True,(255,0,0))
        pygame.display.set_caption("Alien Invasion")
        #makes boss inactive
        self.boss_is_show = False
        # create an instanse to store game statistics
        # and create a scoreboard
        #create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.stars = pygame.sprite.Group()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.Group()
        self.explosion_group_boss = pygame.sprite.Group()
        self.boss_bullets = pygame.sprite.Group()
        self.spaceship = pygame.sprite.Group()
        #START alien invasion in an inactive state
        self.game_active = False
        #make the play button
        self.play_button = Button(self, "Play")
        #self.all_time_high_score = [] using later for saving file results
        self._create_fleet_()
        self._stars()
        self._meteor_obstacle()
    def _create_fleet_(self):
        """create a fleet of aliens"""
        #create an alien and keep ading aliens intil there is no room left
        #spacing between aliens is one alien width
        #spacing between aliens is one alien width and one alien height
        #make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width,alien_height
        while current_y < (self.settings.screen_height-5 * alien_height):
            while current_x < (self.settings.screen_whith - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #finished a row ; reset x value, and increment y value
            current_x = alien_width
            current_y +=2 * alien_height

    def _create_alien(self,x_position, y_position):
            """create am alien and it in the row"""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _update_aliens(self):
        """check if te fleet is at an edge then update positions"""
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _boss_explosion(self):
        if self.boss.boss_hp <= 0:
            self.explosion = Explosion(self.boss.rect.centerx,self.boss.rect.centery, self.settings.boss_img)
            self.explosion_group_boss.add(self.explosion)
        self.explosions = Explosion(self.boss.rect.centerx,self.boss.rect.centery, self.settings.boss_img)
        self.explosion_group_boss.add(self.explosions)

    def _update_meteors(self):
        self.meteor_group.draw(self.screen)
        collide_meteor = pygame.sprite.spritecollide(self.ship,self.meteor_group,True)
        if collide_meteor:
            for collide in collide_meteor:
                meteor_x, meteor_y = collide.rect.centerx, collide.rect.centery
                self.explosions = Explosion(meteor_x,meteor_y, self.settings.meteor_img)
                self.explosion_group.add(self.explosions)
                self._ship_hit_meteor()
                collide.kill()
        if len(self.meteor_group) < 5:
            new_meteor = Meteor(self)
            new_meteor.rect.x = randint(1,1980)
            new_meteor.rect.y = 1
            self.meteor_group.add(new_meteor)

    def _ship_hit_meteor(self):
        """respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships() 
            self.hit.set_volume(0.05)
            self.hit.play()
            # pause
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.lost_game.play()
            
            

    def _check_fleet_edges(self):
        """respnd appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the intire fleet and change the fleets direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _meteor_obstacle(self):#!call method somewhere so meteor dont constantly spawn
        for meteors in range(5):
            new_meteor = Meteor(self)
            new_meteor.rect.x = randint(1,1980)
            new_meteor.rect.y = 1
            self.meteor_group.add(new_meteor)
        
    def _stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width,star_height
        while current_y < (self.settings.screen_height- random_1 * star_height):
            while current_x < (self.settings.screen_whith - random_2 * star_width):
                self._create_stars(current_x, current_y)
                current_x += 2 * star_width
                #finished a row ; reset x value, and increment y value
            current_x = star_width
            current_y += random_3 * star_height

    def _create_stars(self,x_position,y_position):
            """create am alien and it in the row"""
            new_star = Star(self)
            new_star.x = x_position
            new_star.y = y_position
            new_star.rect.x = randint(1,1980)
            new_star.rect.y = randint(1,1000)
            self.stars.add(new_star) 
        
    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        # update bullet position.
        self.bullets.update()
        self.boss_bullets.update()
        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        for boss_bullet_shot in self.boss_bullets.copy():
            if boss_bullet_shot.rect.bottom >= 1200:
                self.boss_bullets.remove(boss_bullet_shot)
        self._check_bullet_alien_collisions()
        self._check_meteor_bullet_colisions()
    
    def _boss_spawn(self):
        """spawns boss every even round"""
        self.boss = Boss(self)
        self.boss_group.add(self.boss)
        self.boss_is_show = False

    def _check_bulets_boss_colision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.boss_group, True, False)  
        if collisions and self.boss.boss_hp > 0:
            self.boss.boss_hp = self.boss.boss_hp - 1
            self._boss_explosion() #! problem 2 - boss_explosion
            print(self.boss.boss_hp)
        if self.boss.boss_hp <= 0:
            self.boss_group.empty()
            self.explosion_group_boss.draw(self.screen)
            self.explosion_group_boss.update()
            self._win()
            self.game_active = False
            pygame.mouse.set_visible(True)

    
    def _check_meteor_bullet_colisions(self):
        bullet_meteor_colisions = pygame.sprite.groupcollide(self.bullets,self.meteor_group,True, False)
    def _ship_boss_bullet_colission(self):
        self.spaceship.add(self.ship)
        ship_boss_colision = pygame.sprite.groupcollide(self.spaceship,self.boss_bullets,False,True) 
        if ship_boss_colision:
            self._ship_hit_meteor()
    def _check_bullet_alien_collisions(self):
         #check for any bullets that hit aliens
        #if so get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy existing bullets and create new fleet
            #self._create_fleet()
            #increase level
            if self.stats.level % 2 != 0:
                self.stats.level += 1
                self.settings.increase_speed()
                self.wave.play()
                self.bullets.empty()  
                self.boss_is_show = True              
            self.sb.prep_level()
        if collisions:
            get_enemies = list(collisions.values())
            for alien_colision in get_enemies:
                enemy_x, enemy_y = alien_colision[0].rect.centerx, alien_colision[0].rect.centery
                self.explosions = Explosion(enemy_x,enemy_y, self.settings.img)
                self.explosion_group.add(self.explosions)
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.Al_death.play()
            self.sb.prep_score()
            self.sb.check_high_score()
    
    def _check_events(self):
        """respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                path = Path("high_score.txt")
                path.write_text(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)    

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            path = Path("high_score.txt")
            path.write_text(str(self.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shot.play()

    def _boss_bullet_attack(self):
        if len(self.boss_bullets) < 3:
            self.boss_bullet = Boss_bullets(self)
            self.boss_bullets.add(self.boss_bullet)
            print("a shot has been made!")
        
    def _update_screen(self):
        #this method is for placing most objects on the screen
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for boss_bullet_shot in self.boss_bullets.sprites():
            boss_bullet_shot.draw_bullet()
        self.ship.blitme()
        if self.stats.level % 2 != 0:
            self.aliens.draw(self.screen)
            self.explosion_group.draw(self.screen)
            self.explosion_group.update()
        # draw the score information
        self.sb.show_score()
        #Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        else:
            self._update_meteors()
        if self.stats.level % 2 == 0:
            print("boss explosions animation",self.explosion_group_boss)
            self.boss_group.draw(self.screen)
            if self.boss_is_show:
                self._boss_spawn()
            self._boss_bullet_attack()
            self.boss_group.update()
            self._check_bulets_boss_colision()
            self._ship_boss_bullet_colission()
            self.explosion_group_boss.draw(self.screen) #! ploblem 3 - draw explosion 
            self.explosion_group_boss.update()
        else:
            self.boss_group.empty()
            
        if self.game_active == False and self.stats.ships_left < 1:
            self._game_over()

        pygame.display.flip()

    def _ship_hit(self):
        """respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships() 
            self.hit.set_volume(0.05)
            self.hit.play()

            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            self.boss_bullets.empty()
            #create a new fleet and center the ship
            if self.stats.level % 2 != 0:
                self._create_fleet()
                self.ship.center_ship()
            # pause
            sleep(0.5)     
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
           
            
            

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # reset the game stetistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            #get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            self.meteor_group.empty()
            #create a new fleet and center the ship
            self._create_fleet_()
            self.ship.center_ship()
            # hide the mouse cursor.
            pygame.mouse.set_visible(False)
            #reset the game settings
            self.settings.initialize_dynamic_settings()

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat this the same as if thhe ship got hit
                self._ship_hit()
                break
    def _game_over(self):
        self.screen.blit(self.loss_line,(800,600))
    def _win(self):
        self.screen.blit(self.winner_line,(800,600))
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                
                self.meteor_group.update()
                self.ship.update()
                self._update_bullets()
                
                if self.stats.level % 2 != 0:
                    self._update_aliens()
                else:
                    self.aliens.empty()
            self._update_screen()
           
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()