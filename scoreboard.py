import pygame.font
from pygame.sprite import Group
from spaceship import Ship 
class Scoreboard:
    """a class to report scoring information"""
    def __init__(self, ai_game):
        """initialize scorekeeping attrebutes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.score_high = pygame.mixer.Sound("sounds/new_highscore.mp3")
        self.score_high.set_volume(0.2)
        self.new_high_score = False
        #font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 100)
        self.loss_line = self.font.render("you lose :(", True, self.text_color)
        #self.boss_defeat = self
        #prepare the initial score image
        #prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """turnthe score into a render image"""
        rounded_score = round(self.stats.score , -1)
        score_str = f"{rounded_score:,}"
        #score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.settings.bg_color)
        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
    
    
    def show_score(self):
        """draw level score and ships on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    def prep_high_score(self):
         #turn the hogh score into a rendered image
        high_score = round(self.stats.high_score ,-1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.settings.bg_color)

        #center the high    score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        """check to see if there a new high score"""
        if (self.stats.score > self.stats.high_score) and self.new_high_score != True:
            self.stats.high_score = self.stats.score
            self.score_high.play()
            self.prep_high_score()
            self.new_high_score = True
            

        if self.stats.score > self.stats.high_score :
            self.stats.high_score = self.stats.score
            self.prep_high_score()
           
            
    def prep_level(self):
        """turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,self.settings.bg_color)
        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        '''show how many ships are left.'''
        self.ships = Group()
        for ship_numbers in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_numbers * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)