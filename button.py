import pygame.font

class Button:
    """a class to build buttons for the game"""

    def __init__(self,ai_game,msg):
        """initialize button attrebutes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimentions and propersies of thhe button
        self.width, self.height = 200, 50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #build the buttons rect object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #the button masage needs to be prepped only once
        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        """turn msg into a rendered image and center text on te button"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """draw blank button and then draw massage"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
