import pygame    
from math import pi    

size = [1050, 750]    
screen = pygame.display.set_mode(size) 
clock = pygame.time.Clock()    
clock.tick(10)    
def table(boxes):  
    """Draws the board"""  
    screen.fill((255, 255, 255))        


    spacebtnboxes=0
    spacebtncircles=0
    fillinthebox=0
    circlefirstscore=0
    fillscoresquare=0
    pygame.draw.rect(screen, (0, 0, 0), [900+spacebtnboxes, 200, 100, 300], 2)
    
    for box2 in range(boxes[0][6]):
        if box2%4==0 and box2!=0:
            fillscoresquare+=20
            circlefirstscore=spacebtnboxes
        pygame.draw.circle(screen, (0, 0, 255), [915+circlefirstscore, 215+fillscoresquare], 10)                
        circlefirstscore+=20
    for box1 in range(6):
        pygame.draw.rect(screen, (0, 0, 0), [200+spacebtnboxes, 130, 100, 200], 2)
        spacebtncircles=spacebtnboxes+15
        fillinthebox=0
        for box2 in range(boxes[0][box1]):
            if box2%5==0 and box2!=0:
                fillinthebox+=17
                spacebtncircles=spacebtnboxes+15
            pygame.draw.circle(screen, (0, 0, 255), [195+spacebtncircles, 145+fillinthebox], 8)
            spacebtncircles+=15
        spacebtnboxes+=110


    spacebtnboxes=0
    spacebtncircles=0
    fillinthebox=0
    pygame.draw.rect(screen, (0, 0, 0), [50+spacebtnboxes, 200, 100, 300], 2)
    for box2 in range(boxes[1][0]):
            if box2%4==0 and box2!=0:
                fillinthebox+=20
                spacebtncircles=spacebtnboxes
            pygame.draw.circle(screen, (0, 0, 255), [65+spacebtncircles, 215+fillinthebox], 10)
            spacebtncircles+=20
    spacebtnboxes=0
    spacebtnboxes=0
    fillinthebox=0
    for box1 in range(6):
        pygame.draw.rect(screen, (0, 0, 0), [200+spacebtnboxes, 400, 100, 200], 2)
        spacebtncircles=spacebtnboxes+15
        fillinthebox=0
        for box2 in range(boxes[1][box1+1]):
            if box2%5==0 and box2!=0:
                fillinthebox+=17
                spacebtncircles=spacebtnboxes+15
            pygame.draw.circle(screen, (0, 0, 255), [200+spacebtncircles, 415+fillinthebox], 8)
            spacebtncircles+=15
        spacebtnboxes+=110
        
    # This function must write after all the other drawing commands.    
    pygame.display.flip()

def drawWinner(boxes):
    """Check who is the winner"""
    screen.fill((255, 255, 255)) 
    font = pygame.font.Font('freesansbold.ttf', 32)
    if boxes[0][6]>boxes[1][0]:
        text = font.render('Player 2 wins!', True, (0, 0, 0))
    elif boxes[0][6]<boxes[1][0]:
        text = font.render('Player 1 wins!', True, (0, 0, 0))
    else:
        text = font.render('Draw!', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1050 // 2, 750 // 2)
    screen.blit(text, textRect)
    pygame.display.flip()