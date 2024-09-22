import pygame
from pygame import mixer 

white=(255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
mixer.init() 
buttonClick=pygame.mixer.Sound('audio/bclick.wav')
class Ui():
    def __init__(self,x, y,w,h,show):
        self.s=show
        
        self.rect=pygame.Rect(x,y,w,h)


        self.clicked = False


    def draw(self, surface):
        action = False
        if self.s==True:
            pygame.draw.rect(surface, red, self.rect)    
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                buttonClick.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


            

        return action