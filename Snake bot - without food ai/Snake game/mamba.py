import pygame
import random

def new_game():
    pygame.init()

    game_display_width = 800
    game_display_height = 600
    
    display_width = 770
    display_height = 570

    gameDisplay = pygame.display.set_mode((game_display_width,game_display_height))
    pygame.display.set_caption('Black mamba')

    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)

    clock = pygame.time.Clock()
    crashed = False
    food = False

    #snake body element
    class sb_block :
        def __init__(self,x,y):
            self.sx = x
            self.sy = y
        def display(self):
            print('sx = ',self.sx)
            print('sy = ',self.sy)

    block_size = 20
    sx = 400
    sy = 300
    head = 0
    body_size = 15

    body = []
    body2 = []

    for i in range(0,body_size):
        body.insert(i,sb_block(sx+i*block_size,sy))
  
    fx = 100
    fy = 100

    step = block_size

    action =1 #default movement to left
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                input('hjhj')

            #detect action
            if event.type == pygame.KEYDOWN:             
                if event.key == pygame.K_LEFT and action!=2:
                    action=1
                elif event.key == pygame.K_RIGHT and action!=1:
                    action=2
                elif event.key == pygame.K_UP and action!=4:
                    action=3
                elif event.key == pygame.K_DOWN and action!=3:
                    action=4
           
        body2.clear()
        for i in range(0,body_size):
            body2.append(sb_block(body[i].sx,body[i].sy))
            
        #perform action (update position of head)      
        if action ==1:
            body[head].sx-=step
        elif action==2:
            body[head].sx+=step
        elif action==3:
            body[head].sy-=step
        elif action==4:
            body[head].sy+=step

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
            #generate new food
            while not food:
                fx = random.randrange(0, 800, block_size)
                fy = random.randrange(0, 600, block_size)
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
            if crashed == True:
                break

        #display updated snake on gamedisplay
        gameDisplay.fill(black)
        #initializing game boundary
        pygame.draw.rect(gameDisplay,green,(15,15,display_width,display_height),1)
        pygame.draw.rect(gameDisplay,red,(body[head].sx,body[head].sy,block_size,block_size),3)

        for i in range(1,body_size):
            pygame.draw.rect(gameDisplay,white,(body[i].sx,body[i].sy,block_size,block_size),i)

        pygame.draw.rect(gameDisplay,green,(fx,fy,block_size,block_size))
        #pygame.draw.rect(gameDisplay,green,(30,30,400,400),1)
        
        score_message('Score :'+str(score))
            
        
            
        pygame.display.update()
        clock.tick(10)

    
    pygame.quit()
    

def main():
    new_game()

main()
quit()
