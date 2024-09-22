import json
import pygame
import tkinter as tk
from UI import Ui
root = tk.Tk()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

usingbg = pygame.image.load("Shop/Assets/Using.png")
buybg = pygame.image.load("Shop/Assets/Buy.png")
buyxbg = pygame.image.load("Shop/Assets/BuyX.png")

usingbg = pygame.transform.scale(usingbg, (screen_width,screen_height))
buybg = pygame.transform.scale(buybg, (screen_width,screen_height))
buyxbg = pygame.transform.scale(buyxbg, (screen_width,screen_height))

sd={}
ows={}

#json file open
px=screen_width/1260
py=screen_height/720

white=(255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)







ship1 = pygame.image.load("Assets/Ships/Ship2.png")
ship1 = pygame.transform.scale(ship1,(140*px,140*py))

ship2 = pygame.image.load("Assets/Ships/Ship1.png")
ship2 = pygame.transform.scale(ship2,(140*px,140*py))


dataJson={}

#json file open
with open('gameData.json') as gd:
    dataJson=json.load(gd)

levelsCompleted=dataJson["levels completed"]
print(levelsCompleted)

ships=[ship1,ship2]
last_button=Ui(200*px,280*py,100*px,100*py,False)
next_button=Ui(980*px,280*py,100*px,100*py,False)
multi_button=Ui(520*px,567*py,220*px,70*py,False)
init=True
ch=0
def ShopScreen(screen,drawtext,sd,ows,pl):
    global init,ch
    if init==True:
        ch=ows["using"]
        init=False

    if ows["isOwned"][ch]==1:
        
        screen.blit(usingbg,(0, 0))
        

        
    else:
        
        if sd["shipData"][ch][2]<=dataJson["gold"]:
            
            screen.blit(buybg,(0, 0))
            ml=multi_button.draw(screen)
            if ml==True:
                ows["isOwned"][ch]=1
                dataJson["gold"]-=sd["shipData"][ch][2]



        else:
            
            screen.blit(buyxbg,(0, 0))
        drawtext(str(sd["shipData"][ch][2]),red,550*px,475*py,int(70*py))

    
    drawtext(str(sd["shipData"][ch][0]),red,130*px,555*py,int(70*py))
    drawtext(str(sd["shipData"][ch][1]),red,1050*px,555*py,int(70*py))
    
    drawtext(str(dataJson["gold"]),red,130*px,160*py,int(70*py))
    bc=last_button.draw(screen)
    fc=next_button.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_d:
                fc=True
            if event.key==pygame.K_a:
                bc=True
            if event.key==pygame.K_ESCAPE:
                pl.health=sd["shipData"][ows['using']][0]
                pl.damage=sd["shipData"][ows['using']][1]
                pl.img=ships[ows['using']]
                return "Home",ows,sd,dataJson,pl
    bc=last_button.draw(screen)
    fc=next_button.draw(screen)
    if bc==True and ch>0:
        ch-=1
    if fc==True and ch<1:
        ch+=1
    if ch==0:
        screen.blit(ship1,(screen_width/2-125/2, 300))
    else:
        screen.blit(ship2,(screen_width/2-125/2, 300))

    
    if ows['isOwned'][ch]==1:
        ows['using']=ch
    return "shop",ows,sd,dataJson,pl

    
