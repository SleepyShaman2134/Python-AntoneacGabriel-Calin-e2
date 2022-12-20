import pygame
import Bot.bot as bot
global start, part

def move_pieces(boxes, number, start, switch, player):
    """
    Moves all the pieces from a box to all the other
    boxes is a 2 dimensional list and the board we work with
    start is the current box
    switch increases or decreases start
    player the player we have at the moment
    """
    if player==1:
        """Choose what part of the board we are"""
        part=1
    else:
        part=0
    if switch==0:
        """
        Check if the box is empty
        """
        if boxes[0][start]==0:
            return 0, start, part
        else:
            boxes[0][start]=0
            """"Empty the box"""
    else:
        """The same as line 18"""
        if boxes[1][start]==0:
            return 0, start, part
        else:
            boxes[1][start]=0
    while number>0:
        """Send all the seeds from the first box to the others"""
        if start==0 and switch==0:
            """Switch path to 1"""
            boxes[1][start]+=1
            switch=1
            part=switch
            number-=1
        if start==6 and switch==1:
            """Switch path to 0"""
            boxes[0][start]+=1
            switch=0
            part=switch
            number-=1
        if switch==1 and number>0:
            """"
            Send seed to the next box
            Setting the part of board we are on
            """
            part=1
            start+=1
            boxes[1][start]+=1
        if switch==0 and number>0:
            """Same as line 47, but set part=0"""
            part=0
            start-=1
            boxes[0][start]+=1
        number-=1
    if part==0 and player==2 and boxes[0][start]==1 and boxes[1][start+1]!=0 and start!=6:
        """Check if player 2 can stole points"""
        boxes[1][0]+=boxes[1][start+1]+boxes[0][start]
        boxes[1][start+1]=0
        boxes[0][start]=0
    if part==1 and player==1 and boxes[1][start]==1 and boxes[0][start-1]!=0 and start!=0:
        """Check if player 1 can stole points"""
        boxes[0][6]+=boxes[1][start]+boxes[0][start-1]
        boxes[1][start]=0
        boxes[0][start-1]=0
    return 1, start, part

def events(done, boxes, player, turn):
    """
    All the events that can happen in the game
    done set it if we have a winner
    boxes the board of boxes
    player the current player active
    turn the current turn we are in
    """
    start=0
    switch=0
    move=-1
    for event in pygame.event.get(): 
        """User did something"""
        switchturn=0
        """variable to check if we change the turn"""
        part=0
        if event.type == pygame.QUIT:
            done = 0
            """The game stops"""
        if turn==1 and player==3:
            """The bot's turn"""
            keep=1
            wincondition1=1
            """Player1 doesn't have seeds on it's side of the board"""
            wincondition2=1
            """Player2 stole the last points from Player1"""
            for box in range(6):
                if boxes[1][box+1]!=0:
                    wincondition1=0
            for box in range(6):
                if boxes[0][box]!=0:
                    wincondition2=0 
            if wincondition1==1:
                for box in range(6):
                        boxes[1][0]+=boxes[0][box]
                return 4, boxes, player, turn
            if wincondition2==1:
                for box in range(6):
                        boxes[0][6]+=boxes[1][box+1]
                return 4, boxes, player, turn
            if keep:
                move=bot.choosemove(boxes)
                """"Bot makes a move between 1 and 6"""
                if move==1:
                    start=0
                    switch=0
                    number=boxes[0][0]
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                elif move==2:
                    start=1
                    switch=0
                    number=boxes[0][1]
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                elif move==3:
                    start=2
                    switch=0
                    number=boxes[0][2]
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                elif move==4:
                    start=3
                    switch=0
                    number=boxes[0][3]
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                elif move==5:
                    start=4
                    switch=0
                    number=boxes[0][4]
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                elif move==6:
                    start=5
                    switch=0
                    number=boxes[0][5]
                    empty, start, part=move_pieces(boxes, move, start, switch, player)
                    if(empty==1):
                        switchturn=1
                        keep=0
                if start==0 and part==1:
                    """Bonus turn if the last piece falls in it's deposit"""
                    switchturn=0
                    keep=1
                if turn==1 and switchturn==1:
                    turn=0
        if player==2 and player!=3 and turn==1:
            wincondition1=1
            wincondition2=1
            for box in range(6):
                if boxes[1][box+1]!=0:
                    wincondition1=0
            for box in range(6):
                if boxes[0][box]!=0:
                    wincondition2=0  
            if wincondition1==1:
                for box in range(6):
                    boxes[1][0]+=boxes[0][box]
                return 4, boxes, player, turn
            if wincondition2==1:
                for box in range(6):
                        boxes[0][6]+=boxes[1][box+1]
                return 4, boxes, player, turn
            if event.type==pygame.KEYDOWN:
                number=0
                if event.key==pygame.K_1:
                    number=boxes[0][0]
                    start=0
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_2:
                    number=boxes[0][1]
                    start=1
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_3:
                    number=boxes[0][2]
                    start=2
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_4:
                    number=boxes[0][3]
                    start=3
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_5:
                    number=boxes[0][4]
                    start=4
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_6:
                    number=boxes[0][5]
                    start=5
                    switch=0
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                if start==0 and part==1:
                    switchturn=0
                if turn==1 and switchturn==1:
                    turn=0
        if player==1 and turn==0:
            """Player1's turn"""
            wincondition1=1
            wincondition2=1
            for box in range(6):
                    if boxes[0][box]!=0:
                        wincondition1=0
            for box in range(6):
                    if boxes[1][box+1]!=0:
                        wincondition2=0   
            if wincondition1==1:
                for box in range(6):
                        boxes[0][6]+=boxes[1][box+1]
                return 4, boxes, player, turn
            if wincondition2==1:
                for box in range(6):
                        boxes[1][0]+=boxes[0][box]
                return 4, boxes, player, turn
            if event.type==pygame.KEYDOWN:
                number=0
                if event.key==pygame.K_1:
                    number=boxes[1][1]
                    start=1
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_2:
                    number=boxes[1][2]
                    start=2
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_3:
                    number=boxes[1][3]
                    start=3
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_4:
                    number=boxes[1][4]
                    start=4
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_5:
                    number=boxes[1][5]
                    start=5
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                elif event.key==pygame.K_6:
                    number=boxes[1][6]
                    start=6
                    switch=1
                    empty, start, part=move_pieces(boxes, number, start, switch, player)
                    if(empty==1):
                        switchturn=1
                if start==6 and part==0:
                    switchturn=0
                if turn==0 and switchturn==1:            
                    turn=1
    return done, boxes, player, turn