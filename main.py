import pygame
import json
import gameloops
from pygame import mixer 
import asyncio
import random
import tkinter as tk
import shopS
from UI import Ui
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

px=screen_width/1260
py=screen_height/720
#loading sound
mixer.init() 

shotSound=pygame.mixer.Sound('audio/shot.wav')
explosionSound=pygame.mixer.Sound('audio/explosion.wav')
bgm=pygame.mixer.Sound('audio/bg_music.mp3')

with open('Shop/Scripts/ShipData.json') as gd:
    sd=json.load(gd)
with open('Shop/Scripts/OwningStatus.json') as gd:
    ows=json.load(gd)

bgm.play(-1)
white=(255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

#loading background
bg = pygame.image.load("Assets/Background/bg.png")
bg = pygame.transform.scale(bg, (screen_width,screen_height))
bg2 = pygame.image.load("Assets/Background/bg2.jpg")
bg2 = pygame.transform.scale(bg2, (screen_width,screen_height))
bg3 = pygame.image.load("Assets/Background/winScreen.png")
bg3 = pygame.transform.scale(bg3, (screen_width,screen_height))
#loading bullet
bullet1 = pygame.image.load("Assets/bullets/BulletE.png")
bullet1 = pygame.transform.scale(bullet1, (30*px,10*py))
bullet1 = pygame.transform.rotate(bullet1, -90)
#loading the ships


ship1 = pygame.image.load("Assets/Ships/Ship2.png")
ship1 = pygame.transform.scale(ship1,(140*px,140*py))

ship2 = pygame.image.load("Assets/Ships/Ship1.png")
ship2 = pygame.transform.scale(ship2,(140*px,140*py))

ships=[ship1,ship2]

Enemyship1 = pygame.image.load("Assets/Ships/EnemyShip1.png")
Enemyship1 = pygame.transform.scale(Enemyship1, (140*px,140*py))
Enemyship1 = pygame.transform.rotate(Enemyship1,180)

Enemyship2 = pygame.image.load("Assets/Ships/EnemyShip2.png")
Enemyship2 = pygame.transform.scale(Enemyship2, (140*px,140*py))
Enemyship2 = pygame.transform.rotate(Enemyship2,180)

class Button():
	def __init__(self,x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False

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

		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
     

#creating the screen
pygame.init()
screen = pygame.display.set_mode((1265*px, 720*py), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

#creating font
font = pygame.font.Font('freesansbold.ttf', 64)
text = font.render('Cosmic Clash', True, green)
textRect = text.get_rect()
textRect.center = (620*px,50*py)

font = pygame.font.Font('freesansbold.ttf', 32)
level_text = font.render('Prepare for the ultimate interstellar showdown!', True, red)
level_textRect = level_text.get_rect()
level_textRect.center = (600*px,50*py)

#loading button images
back = pygame.image.load("Assets/Buttons/back.png")
shop = pygame.image.load("Assets/Buttons/shop.png")
start = pygame.image.load("Assets/Buttons/start.png")
start = pygame.transform.scale(start, (start.get_width()*px,start.get_height()*py-(10*py)))
shop = pygame.transform.scale(shop, (shop.get_width()*px,shop.get_height()*py-(10*py)))

#creating the buttons
start_button=Ui(525*px,380*py,210*px,100*py,False)
shop_button=Ui(443*px,330*py,100*px,100*py,True)
back_button=Ui(1100*px,600*py,130*px,100*py,False)
home_button=Ui(40*px,600*py,100*px,100*py,False)

#loading level buttons
l1 = pygame.image.load("Assets/level/1.png")
l2 = pygame.image.load("Assets/level/2.png")
l3 = pygame.image.load("Assets/level/3.png")
l4 = pygame.image.load("Assets/level/4.png")
l5 = pygame.image.load("Assets/level/5.png")
l6 = pygame.image.load("Assets/level/6.png")
l7 = pygame.image.load("Assets/level/7.png")
l8 = pygame.image.load("Assets/level/8.png")

#levels
button_l1=Button(150*px,130*py,l1,0.26)
button_l2=Button(400*px,130*py,l2,0.26)
button_l3=Button(650*px,130*py,l3,0.26)
button_l4=Button(900*px,130*py,l4,0.26)
button_l5=Button(150*px,330*py,l5,0.26)
button_l6=Button(400*px,330*py,l6,0.26)
button_l7=Button(650*px,330*py,l7,0.26)
button_l8=Button(900*px,330*py,l8,0.26)

#creating font blueprint
font = pygame.font.SysFont('Futura', 30)
font2 = pygame.font.SysFont('Futura', 70)

def draw_text(text,text_col, x, y,txtsize):
    font = pygame.font.SysFont('Futura', txtsize)
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

game_state="Home"

#creating player spaceship coordinates
pl_x=650*px
pl_y=600*py
gameovertick=0

#creating groups
bulletGroup=pygame.sprite.Group()        
EnemyGroup=pygame.sprite.Group()
PlayerbulletGroup=pygame.sprite.Group()
explosion_group=pygame.sprite.Group()
buttonClick=pygame.mixer.Sound('audio/bclick.wav')

#create enemy blueprint
class bullet(pygame.sprite.Sprite):
    def __init__(self,image,speed,x,y,dam,targetX,targetY,dy,entity):
        pygame.sprite.Sprite.__init__(self)
        self.x=x+(55*px)
        self.y=y+dy
        self.img=image
        self.speed=speed
        self.playerx=targetX+(55*px)
        self.playery=targetY
        self.dam=dam
        self.yChange=((self.playery-self.y)/1000)*self.speed
        self.xChange=((self.playerx-self.x)/1000)*self.speed
        self.rect = self.img.get_rect()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect.center = (self.width/2, self.height/2)
        self.entity=entity
        
    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y
        screen.blit(self.img,(self.x,self.y))
       
        self.x+=self.xChange
        self.y+=self.yChange
        if pygame.sprite.collide_rect(pl,self) and self.entity=="enemy":
            
            pl.health-=self.dam
            self.kill()
        if self.entity=="player":
            for i in EnemyGroup:
                if pygame.sprite.collide_rect(i,self):
                    i.health-=100
                    self.kill()

        if self.y>1500:
            self.kill()

#creating player bullets
class Plbullet(pygame.sprite.Sprite):
    def __init__(self,image,speed,x,y,dam):
        pygame.sprite.Sprite.__init__(self)
        self.x=x+(50*px)
        self.y=y+(10*py)
        self.img=image
        self.speed=speed
        self.rect = self.img.get_rect()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect.center = (self.width/2, self.height/2)
        self.dam=dam
        
        
        
        
    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y
        screen.blit(self.img,(self.x,self.y))
        
        self.y-=6*self.speed

        
        
        for i in EnemyGroup:
            if pygame.sprite.spritecollide(i,PlayerbulletGroup, False):
                
                i.health-=self.dam
                self.kill()
                
        
        if self.y<0:
            self.kill()
#creating explosion blueprint
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f'Assets/explosion/exp{num}.png').convert_alpha()
			img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
			self.images.append(img)
		self.frame_index = 0
		self.image = self.images[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.counter = 0
        
        

	def update(self):
		#scroll
		screen.blit(self.images[self.frame_index],(self.rect.x,self.rect.y))

		EXPLOSION_SPEED = 4
		#update explosion amimation
		self.counter += 1

		if self.counter >= EXPLOSION_SPEED:
			self.counter = 0
			self.frame_index += 1
			#if the animation is complete then delete the explosion
			if self.frame_index >= len(self.images):
				self.kill()
			else:
				self.image = self.images[self.frame_index]



#creating player blueprint
class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xpos=x
        self.ypos=y
        self.img=ships[ows["using"]]
        self.health=sd["shipData"][ows['using']][0]
        self.isalive=True
        self.rect = self.img.get_rect()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rect.center = (self.width/2, self.height/2)
        self.enemyTakedown=0
        self.shootCooldown=0
        self.abilityLoader=0
        self.useAbility=False
        self.initHealth=sd["shipData"][ows['using']][0]
        self.damage=sd["shipData"][ows['using']][1]
        
    def update(self):
        if self.abilityLoader<100:
            self.abilityLoader+=0.05
        if self.shootCooldown>0:
            self.shootCooldown-=1
        self.rect.x=self.xpos-20
        self.rect.y=self.ypos
        if self.health<=0:
            self.isalive=False
        if self.isalive==True:
            screen.blit(self.img,(self.xpos,self.ypos))
            
        return "game"
        
    def ability(self):
        r1=pygame.Rect(10*px,150*py,100*px,20*py)
        r2=pygame.Rect(10*px,150*py,self.abilityLoader*px,20*py)
        
        pygame.draw.rect(screen,red,r2)
        pygame.draw.rect(screen, white, r1,2)

        if pl.useAbility==True:
            for i in EnemyGroup:
                if i.x_pos>20:
                    bt=bullet(bullet1,45,self.xpos,self.ypos,100,i.x_pos,i.y_pos,0,"player")
                    bulletGroup.add(bt)

            pl.useAbility=False
                
                  



#creating enemy blueprint              
class enemy(pygame.sprite.Sprite):
    def __init__(self,health,dam,img):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos=(random.randrange(100,1000))*px
        self.y_pos=(-300)*py
        self.image=img
        self.health=health
        self.damage=dam
        self.direction=random.randrange(-10,10)
        print(self.direction)
        if self.direction>0:
            self.direction=1
        else:
            self.direction=-1

        self.counter=100
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.center = (self.width/2, self.height/2)
    def update(self):
        self.rect.x=self.x_pos
        self.rect.y=self.y_pos
        screen.blit(self.image,self.rect)
        
        
        if self.y_pos<(100*py):
            self.y_pos+=5
            self.counter=0
        else:
            self.shoot()
            self.counter+=1
            self.movement()

        if self.health<=0:
            self.kill()
            pl.enemyTakedown+=1
            explosion = Explosion(self.rect.x, self.rect.y, 2)
            explosion_group.add(explosion)
            explosionSound.play()

    def shoot(self):
        if self.counter==75:
            
            bt=bullet(bullet1,7,self.x_pos,self.y_pos,self.damage,pl.xpos,pl.ypos,140*py,"enemy")
            bulletGroup.add(bt)
            self.counter=0
    def movement(self):
        if self.x_pos<0:
            self.direction=1
        elif self.x_pos>1000*px:
            self.direction=-1
        self.x_pos+=2*self.direction
    

#game variables
setup=False

pl=player(pl_x,pl_y)

cnt=0

game_state="game"
ScreenState="Home"

levelsCompleted=0
dataJson={}

#json file open
with open('gameData.json') as gd:
    dataJson=json.load(gd)

levelsCompleted=dataJson["levels completed"]
print(levelsCompleted)

#game page


    
    
#declaring control variables
left_keyDown=False   
Right_keyDown=False   

shot=False

enemycount=0
async def main():
    global pl,running,ScreenState,levelChoise,enemycount,lvlEnemyCont,gameovertick,dataJson,game_state,left_keyDown,Right_keyDown,cnt,sd,ows
    while running:
        
        if ScreenState=="Home":
            ScreenState=gameloops.Home(start_button,screen,bg)
        elif ScreenState=="level":
            ScreenState,levelChoise,enemycount=gameloops.level(screen,back_button,bg,bg2,level_text,level_textRect,dataJson,button_l1,button_l2,button_l3,button_l4,button_l5,button_l6,button_l7,button_l8,px,py,pl,ows,sd)
            lvlEnemyCont=enemycount
            pl.abilityLoader=0
        elif ScreenState=="shop":
            ScreenState,ows,sd,dataJson,pl=shopS.ShopScreen(screen,draw_text,sd,ows,pl)
        elif ScreenState=="game":
            enemycount,game_state,ScreenState,gameovertick=gameloops.Game(cnt,enemycount,lvlEnemyCont,game_state,levelChoise,gameovertick,bgm,screen,explosion_group,bulletGroup,PlayerbulletGroup,EnemyGroup,pl,enemy,Enemyship1,Enemyship2,ScreenState,draw_text,white,px,py,dataJson,font,font2,home_button,back_button,bg3,blue)
            
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                with open('gameData.json','w') as gdw:
                    json.dump(dataJson,gdw)
                with open('Shop/Scripts/ShipData.json','w') as gd:
                    json.dump(sd,gd)
                with open('Shop/Scripts/OwningStatus.json','w') as gd:
                    json.dump(ows,gd)
                running = False
            if game_state=="game":
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        Right_keyDown=True
                        left_keyDown=False
                    if event.key==pygame.K_LEFT:
                        left_keyDown=True
                        Right_keyDown=False
                    if event.key==pygame.K_SPACE:
                        if pl.shootCooldown==0:
                            blt=Plbullet(bullet1,3,pl.xpos,pl.ypos,pl.damage)
                            PlayerbulletGroup.add(blt)
                            pl.shootCooldown=50         
                            shotSound.play()
                    if event.key==pygame.K_ESCAPE and ScreenState!='shop':
                        with open('gameData.json','w') as gdw:
                            json.dump(dataJson,gdw)
                        with open('Shop/Scripts/ShipData.json','w') as gd:
                            json.dump(sd,gd)
                        with open('Shop/Scripts/OwningStatus.json','w') as gd:
                            json.dump(ows,gd)
                        running = False
                    if event.key==pygame.K_e and pl.abilityLoader>99:
                        print("True ")
                        pl.abilityLoader=0
                        pl.useAbility=True
                    else :
                        print(pl.abilityLoader)
                         
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        Right_keyDown=False
                        
                    if event.key==pygame.K_LEFT:
                        left_keyDown=False
                        
                        
        if left_keyDown==True and pl.xpos-5>=0:
            pl.xpos-=5*px
        if Right_keyDown==True and (pl.xpos+pl.rect.width)+5<=1260*py:
            pl.xpos+=5*px
        

    
        pygame.display.flip()
        
        clock.tick(100)  
        cnt+=1
    pygame.quit()
    await asyncio.sleep(0)

asyncio.run(main())