import pygame
import tkinter as tk
from UI import Ui
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bg4 = pygame.image.load("Assets/Background/LosingScreenBg.png")
bg4 = pygame.transform.scale(bg4, (screen_width,screen_height))

px=screen_width/1260
py=screen_height/720

starimg = pygame.image.load("Assets/level/star.png")
starimg=pygame.transform.scale(starimg,(40*px,40*py))

shop_button=Ui(750*px,370*py,100*px,100*py,False)
def Home(start_button,screen,bg):   
    start_button,screen
    screen.blit(bg, (0, 0))

    
    stc=start_button.draw(screen)
    #shc=shop_button.draw(screen)
    shc=shop_button.draw(screen)
    if stc==True:
        return "level"
    elif shc==True:
        return "shop"
    return "Home"
    
        
        
        
#level page
def level(screen,back_button,bg,bg2,level_text,level_textRect,dataJson,button_l1,button_l2,button_l3,button_l4,button_l5,button_l6,button_l7,button_l8,px,py,pl,ows,sd):

    screen.blit(bg2, (0, 0))
    screen.blit(level_text, level_textRect)
    lv1=False
    lv2=False
    lv3=False
    lv4=False
    lv5=False
    lv6=False
    lv7=False
    lv8=False

    c=0
    for i in range (dataJson['levels completed']):
        
        lvst=dataJson["stars"]
        lvst=lvst[i]
        dy=(i//4)
        
        
        
        if lvst[0]=='True':
            screen.blit(starimg, ((150+(c*250))*px,110*py+(200*dy)))
        if lvst[1]=='True':
            screen.blit(starimg, ((200+(c*250))*px,90*py+(200*dy)))
        if lvst[2]=='True':
            screen.blit(starimg, ((250+(c*250))*px,110*py+(200*dy)))
        c+=1
        if c%4==0:
            c=0
        
    if dataJson['levels completed']>=7:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
        lv4=button_l4.draw(screen)
        lv5=button_l5.draw(screen)
        lv6=button_l6.draw(screen)
        lv7=button_l7.draw(screen)
        lv8=button_l8.draw(screen)
    elif dataJson['levels completed']>=6:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
        lv4=button_l4.draw(screen)
        lv5=button_l5.draw(screen)
        lv6=button_l6.draw(screen)
        lv7=button_l7.draw(screen)
    elif dataJson['levels completed']>=5:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
        lv4=button_l4.draw(screen)              
        lv5=button_l5.draw(screen)
        lv6=button_l6.draw(screen)
    elif dataJson['levels completed']>=4:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
        lv4=button_l4.draw(screen)
        lv5=button_l5.draw(screen)    
    elif dataJson['levels completed']>=3:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
        lv4=button_l4.draw(screen)
    elif dataJson['levels completed']>=2:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
        lv3=button_l3.draw(screen)
    elif dataJson['levels completed']>=1:
        lv1=button_l1.draw(screen)
        lv2=button_l2.draw(screen)
    elif dataJson['levels completed']>=0:
        lv1=button_l1.draw(screen)
    
    if lv1==True or lv2==True or lv3==True or lv4==True or lv5==True or lv6==True or lv7==True or lv8==True  :
        pass

    if lv1==True:
        
        return "game",1,8
    elif lv2==True:
        
        return "game",2,8
    elif lv3==True:
        return "game",3,10
    elif lv4==True:
        return "game",4,12
    elif lv5==True:
        return "game",5,8
    elif lv6==True:
        return "game",6,8
    elif lv7==True:
        return "game",7,10
    elif lv8==True:
        
        return "game",8,12
    
     
    return "level",0,0
    


#shop page
def shop(screen,back_button,bg):
    
    screen.blit(bg, (0, 0))
    bc=back_button.draw(screen)
    if bc==True:
        return "Home"
    return "shop"

def Game(counter,enemycount,initEnemyCount,game_state,lvl,gameovertick,bgm,screen,explosion_group,bulletGroup,PlayerbulletGroup,EnemyGroup,pl,enemy,Enemyship1,Enemyship2,ScreenState,draw_text,white,px,py,dataJson,font,font2,home_button,back_button,bg3,blue):
    bgm.stop()
    gold=0
    if game_state=="game":
        screen.fill((0,0,0))
                
        explosion_group.update()
        bulletGroup.update()
        PlayerbulletGroup.update()
        EnemyGroup.update()
        game_state=pl.update()
        pl.ability()
        if lvl==1:

                if counter%350==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(10,7,Enemyship1)
                    EnemyGroup.add(enemy1)
                    
                    enemycount-=1
                
        if lvl==2:

                if counter%350==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(10,8,Enemyship1)
                    EnemyGroup.add(enemy1)
                    
                    enemycount-=1
                
        if lvl==3:
                if counter%400==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(15,8,Enemyship2)
                    EnemyGroup.add(enemy1)
                    
                    
                    enemycount-=1
                
                
        if lvl==4:
                if counter%400==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(15,9,Enemyship2)
                    EnemyGroup.add(enemy1)
                    
                    
                    enemycount-=1
                
                
        if lvl==5:
            
                if counter%500==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(10,5,Enemyship1)
                    EnemyGroup.add(enemy1)
                    print(counter)
                    enemy1=enemy(10,5,Enemyship1)
                    EnemyGroup.add(enemy1)
                    
                    enemycount-=2
                
        if lvl==6:

                if counter%400==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(10,6,Enemyship1)
                    EnemyGroup.add(enemy1)
                    print(counter)
                    enemy1=enemy(10,6,Enemyship1)
                    EnemyGroup.add(enemy1)
                    
                    enemycount-=2
                
        if lvl==7:

                if counter%700==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(15,6,Enemyship2)
                    EnemyGroup.add(enemy1)
                    enemy1=enemy(15,6,Enemyship2)
                    EnemyGroup.add(enemy1)
                    
                    
                    enemycount-=2
                
        if lvl==8:

                if counter%500==0 and enemycount>0:
                    print(counter)
                    enemy1=enemy(15,7,Enemyship2)
                    EnemyGroup.add(enemy1)
                    enemy1=enemy(15,7,Enemyship2)
                    EnemyGroup.add(enemy1)
                    
                    
                    enemycount-=2
                
        draw_text("Health:"+str(pl.health),white,10*px,10*py,int(30*py))
        draw_text("Enemys left:"+str(initEnemyCount-pl.enemyTakedown),white,10*px,40*py,int(30*py))
        if pl.enemyTakedown==initEnemyCount or pl.isalive==False:
            gameovertick-=1
            if gameovertick==0:
                if pl.isalive==True:
                    star=dataJson["stars"]
                    stardiv=star[lvl-1] 
                    
                    star1=stardiv[0]
                    star2=stardiv[1] 
                    star3=stardiv[2]  
                    if star1=='False' and pl.health>=pl.initHealth/4:
                        star1='True'
                        gold+=50
                    if star2=='False' and pl.health>=pl.initHealth/3:
                        star2='True'
                        gold+=50
                    if star3=='False' and pl.health>=pl.initHealth/2:
                        star3='True'
                        gold+=50
                    stardiv=[star1,star2,star3]
                    star[lvl-1]=stardiv
                    dataJson["stars"]=star
                    
                    gld=((lvl//4)+1)*(initEnemyCount//2)
                    gold+=pl.enemyTakedown*gld
                    print(gold)
                    
                    dataJson["gold"]+=gold
                    dataJson["Gold lg"]=gold

                    game_state="won"
                else:
                    gld=((lvl//4)+1)*(initEnemyCount//2)
                    gold+=pl.enemyTakedown*gld
                    print(gold)
                    
                    dataJson["gold"]+=gold
                    dataJson["Gold lg"]=gold
                    game_state="lost"
        
        else:
            gameovertick=100            
        return enemycount,game_state,ScreenState,gameovertick
    

    if game_state=="won":
        
        screen.blit(bg3, (0, 0))
        
        
        draw_text(str(pl.enemyTakedown),white,630*px,325*py,int(70*py))
        draw_text(str(dataJson["Gold lg"]),white,630*px,400*py,int(70*py))
        if dataJson["levels completed"]<lvl:
            dataJson["levels completed"]=lvl

        hc=home_button.draw(screen)
        bc=back_button.draw(screen)
       
        if bc==True or hc==True:
            dataJson["Gold lg"]=0
            pl.health=100
            pl.isalive=True
            pl.enemyTakedown=0
            for i in EnemyGroup:
                i.kill()
            for i in PlayerbulletGroup:
                i.kill()
            for i in bulletGroup:
                i.kill()
            
            if bc==True:
                bgm.play(-1)
                return 0,"game","level",0
            else:
                bgm.play(-1)
                return 0,"game","Home",0

        
        return 0,game_state,ScreenState,gameovertick
    
    else:
        
        screen.blit(bg4, (0, 0))
        draw_text(str(pl.enemyTakedown),white,630*px,310*py,int(70*py))
        draw_text(str(dataJson["Gold lg"]),white,630*px,370*py,int(70*py))
        hc=back_button.draw(screen)
        bc=home_button.draw(screen)
        if hc==True or bc == True:
            pl.health=100
            pl.isalive=True
            pl.enemyTakedown=0
            for i in EnemyGroup:
                i.kill()
            for i in PlayerbulletGroup:
                i.kill()
            for i in bulletGroup:
                i.kill()
            if hc==True:
                return 0,"game","Home",0
            else:
                return 0,"game","level",0
        return 0,game_state,ScreenState,gameovertick

    