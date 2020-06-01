import pygame
import random
import numpy as np
import dtree as ai


def new_game():
    pygame.init()

    game_display_width = 800
    game_display_height = 600
    
    
    gameDisplay = pygame.display.set_mode((game_display_width,game_display_height))
    pygame.display.set_caption('Black mamba')

    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)

    clock = pygame.time.Clock()
    crashed = False
    food = False
    action_found = False

    #snake body element
    class sb_block :
        def __init__(self,x,y):
            self.sx = x
            self.sy = y
        def display(self):
            print('sx = ',self.sx)
            print('sy = ',self.sy)

    block_size = 20
    display_width = game_display_width - block_size
    display_height = game_display_height - block_size
    sx = 400
    sy = 300
    head = 0
    body_size = 14

    body = []
    body2 = []
    
    #generate default action and initialise snake body
    action = random.randrange(1,5,1)
    if action==1 :     #default action is LEFT
        for i in range(0,body_size):
            body.insert(i,sb_block(sx+i*block_size,sy))
    elif action==2 :     #default action is RIGHT
        for i in range(0,body_size):
            body.insert(i,sb_block(sx-i*block_size,sy))
    elif action==3 :     #default action is UP
        for i in range(0,body_size):
            body.insert(i,sb_block(sx,sy+i*block_size))
    elif action==4 :     #default action is DOWN
        for i in range(0,body_size):
            body.insert(i,sb_block(sx,sy-i*block_size))

    #generate initial food position  
    fx = 5*block_size
    fy = 5*block_size

    previous_action = action
    score = 0

    #for displaying text
    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        

    def score_message(text):
        largeText = pygame.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (50,10)
        gameDisplay.blit(TextSurf, TextRect)

    #initializing game--frame 0
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay,red,(body[head].sx,body[head].sy,block_size,block_size))

    for i in range(1,body_size):
        pygame.draw.rect(gameDisplay,white,(body[i].sx,body[i].sy,block_size,block_size))
    pygame.draw.rect(gameDisplay,green,(fx,fy,block_size,block_size))
    score_message('Score : 0')

    #game loop
    while not crashed:
        #direction variables
        #1.WEST
        w_wall = body[head].sx

        if body[head].sy==fy and body[head].sx>fx:
            w_food = body[head].sx - fx
        else:
            w_food = -1
                
        for i in range(1,body_size) :
            if body[head].sy==body[i].sy and body[head].sx>body[i].sx:
                w_body = body[head].sx - body[i].sx
                break
            else:
                w_body = -1
                
        #2.NORTH
        n_wall = body[head].sy

        if body[head].sx==fx and body[head].sy>fy:
            n_food = body[head].sy - fy
        else:
            n_food = -1
                
        for i in range(1,body_size) :
            if body[head].sx==body[i].sx and body[head].sy>body[i].sy:
                n_body = body[head].sy - body[i].sy
                break
            else:
                n_body = -1             
                
        #3.NORTHWEST
        if n_wall<w_wall :
            nw_wall = 1.414*n_wall
        else :
            nw_wall = 1.414*w_wall

        x = body[head].sx - block_size
        y = body[head].sy - block_size

        
        while x > -1 :
            if x==fx and y==fy:
                if fx<fy :
                    f_wall = 1.414*fx
                else :
                    f_wall = 1.414*fy
                nw_food = nw_wall - f_wall
                break
            else:
                nw_food = -1
            x = x - block_size
            y = y - block_size

        body_found = False
        x = body[head].sx - block_size
        y = body[head].sy - block_size
        while x > -1 :
            for i in range(1,body_size):
                if x==body[i].sx and y==body[i].sy:
                    if body[i].sx<body[i].sy :
                        b_wall = 1.414*body[i].sx
                    else :
                        b_wall = 1.414*body[i].sy
                    nw_body = nw_wall - b_wall
                    body_found = True
                    break
            if body_found==True:
                break
            else:
                nw_body = -1
            x = x - block_size
            y = y - block_size
            
                
        #4.EAST
        e_wall = display_width - body[head].sx

        if body[head].sy==fy and body[head].sx<fx:
            e_food = fx - body[head].sx
        else:
            e_food = -1
                
        for i in range(1,body_size) :
            if body[head].sy==body[i].sy and body[head].sx<body[i].sx:
                e_body = body[i].sx - body[head].sx
                break
            else:
                e_body = -1            
           
                
                
        #5.NORTHEAST
        if n_wall<e_wall :
            ne_wall = 1.414*n_wall
        else :
            ne_wall = 1.414*e_wall
        
        x = body[head].sx + block_size
        y = body[head].sy - block_size
        while x < display_width+1 and y > -1 :
            if x==fx and y==fy:
                if (display_width-fx)<fy :
                    f_wall = 1.414*(display_width-fx)
                else :
                    f_wall = 1.414*fy
                ne_food = ne_wall - f_wall
                break
            else:
                ne_food = -1
            x = x + block_size
            y = y - block_size

        body_found = False
        x = body[head].sx + block_size
        y = body[head].sy - block_size
        while x < display_width+1 and y > -1:
            for i in range(1,body_size):
                if x==body[i].sx and y==body[i].sy:
                    if (display_width-body[i].sx)<fy :
                        b_wall = 1.414*(display_width-body[i].sx)
                    else :
                        b_wall = 1.414*body[i].sy
                    ne_body = ne_wall - b_wall
                    body_found = True
                    break
            if body_found==True:
                break
            else:
                ne_body = -1
            x = x + block_size
            y = y - block_size        

                
            
        #6.SOUTH
        s_wall = display_height - body[head].sy

        if body[head].sx==fx and body[head].sy<fy:
            s_food = fy - body[head].sy
        else:
            s_food = -1
                
        for i in range(1,body_size) :
            if body[head].sx==body[i].sx and body[head].sy<body[i].sy:
                s_body = body[i].sy - body[head].sy
                break
            else:
                s_body = -1         
                
        #7.SOUTHEAST
        if s_wall<e_wall :
            se_wall = 1.414*s_wall
        else :
            se_wall = 1.414*e_wall        

        x = body[head].sx + block_size
        y = body[head].sy + block_size
        while x < (display_width-1) and y < (display_height-1) :
            if x==fx and y==fy:
                if (display_width-fx)<(display_height-fy) :
                    f_wall = 1.414*(display_width-fx)
                else :
                    f_wall = 1.414*(display_height-fy)
                se_food = se_wall - f_wall
                break
            else:
                se_food = -1
            x = x + block_size
            y = y + block_size

        body_found = False
        x = body[head].sx + block_size
        y = body[head].sy + block_size
        while x < display_width-1 and y < display_height-1 :
            for i in range(1,body_size):
                if x==body[i].sx and y==body[i].sy:
                    if (display_width-body[i].sx)<(display_height-body[i].sy) :
                        b_wall = 1.414*(display_width-body[i].sx)
                    else :
                        b_wall = 1.414*(display_height-body[i].sy)
                    se_body = se_wall - b_wall
                    body_found = True
                    break
            if body_found==True:
                break
            else:
                se_body = -1
            x = x + block_size
            y = y + block_size
                
                
                
               
                
                
        #8.SOUTHWEST
        if s_wall<w_wall :
            sw_wall = 1.414*s_wall
        else :
            sw_wall = 1.414*w_wall 
        
        x = body[head].sx - block_size
        y = body[head].sy + block_size
        while x > -1 and y < (display_height-1) :
            if x==fx and y==fy:
                if fx<(display_height-fy) :
                    f_wall = 1.414*fx
                else :
                    f_wall = 1.414*(display_height-fy)
                sw_food = sw_wall - f_wall
                break
            else:
                sw_food = -1
            x = x - block_size
            y = y + block_size

        body_found = False
        x = body[head].sx - block_size
        y = body[head].sy + block_size
        while x > -1 and y < display_height-1 :
            for i in range(1,body_size):
                if x==body[i].sx and y==body[i].sy:
                    if body[i].sx<(display_height-body[i].sy) :
                        b_wall = 1.414*body[i].sx
                    else :
                        b_wall = 1.414*(display_height-body[i].sy)
                    sw_body = sw_wall - b_wall
                    body_found = True
                    break
            if body_found==True:
                break
            else:
                sw_body = -1
            x = x - block_size
            y = y + block_size


        body2.clear()
        for i in range(0,body_size):
            body2.append(sb_block(body[i].sx,body[i].sy))
            
        #predict action using ann
        action_found = False
        while not action_found :
            action =  random.randrange(1, 5, 1)
            if (action==2 and previous_action==1) or (action==1 and previous_action==2) or (action==3 and previous_action==4)or (action==4 and previous_action==3):
                action = previous_action
            
            # prediction = predict(action)
            list = np.array([w_wall,w_body, nw_wall,nw_body ,n_wall,n_body ,
                            ne_wall,ne_body ,e_wall,e_body ,se_wall,se_body ,
                            s_wall,s_body ,sw_wall,sw_body ,action])
            list = list.reshape((1,list.shape[0]))
            
            prediction = ai.predictor(list)
            if prediction == True:
                action_found=True
        
        #perform action (update position of head)      
        if action ==1:
            body[head].sx-=block_size
        elif action==2:
            body[head].sx+=block_size
        elif action==3:
            body[head].sy-=block_size
        elif action==4:
            body[head].sy+=block_size

        #update positions of body blocks
        j=0
        for i in range(1,body_size):
            body[i].sx = body2[j].sx
            body[i].sy = body2[j].sy
            j+=1
    
        #detect wall crash
        if body[head].sx<15 or body[head].sy<15 or body[head].sx>display_width-10 or body[head].sy>display_height-10:
            crashed = True
            message_display('noob')
            pygame.display.update()
            break
            
        #detect if snake found food
        if body[head].sx==fx and body[head].sy==fy:
            body.insert(head,sb_block(fx,fy))
            body_size+=1
            score+=1
            reward = 10
            #generate new food
            while not food:
                fx = random.randrange(block_size, display_width, block_size)
                fy = random.randrange(block_size, display_height, block_size)
                food = True
                for i in range(0,body_size):
                    if body[i].sx == fx and body[i].sy == fy :
                        food = False
                        break
            food = False
            
            print('food hunted'+str(score))
            
        #detect body crash
        else:
            for i in range(1,body_size):
                if body[head].sx == body[i].sx and body[head].sy == body[i].sy:
                    crashed = True
                    message_display('noob')
                    pygame.display.update()
                    print('body crash'+str(i)        )
                    print(action)
                    print(body[head].sx)
                    print(body[head].sy)
                    print(body[i].sx)
                    print(body[i].sy)
                    break
                    
            

        #display updated snake on gamedisplay
        gameDisplay.fill(black)
        #initializing game boundary
        pygame.draw.rect(gameDisplay,green,(block_size,block_size,display_width-block_size,display_height-block_size),1)
        pygame.draw.rect(gameDisplay,red,(body[head].sx,body[head].sy,block_size,block_size),3)

        for i in range(1,body_size):
            pygame.draw.rect(gameDisplay,white,(body[i].sx,body[i].sy,block_size,block_size),1)

        pygame.draw.rect(gameDisplay,green,(fx,fy,block_size,block_size))
        #pygame.draw.rect(gameDisplay,green,(30,30,400,400),1)
        
        score_message('Score :'+str(score))
        
        if crashed==True:
            break
        previous_action = action
        pygame.display.update()
        clock.tick(10)

    #pygame.time.delay(5000)
    pygame.quit()
    
    

def main():
    for i in range(10):
        new_game()
        

main()
    
