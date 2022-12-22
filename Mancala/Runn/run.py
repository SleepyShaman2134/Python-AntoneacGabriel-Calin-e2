import sys
import pygame 
from math import pi  
import Table.table as table
import Event.event as event

boxes=[[4, 4, 4, 4, 4, 4, 0],[0, 4, 4, 4, 4, 4, 4]]
"""The board that we will play on"""
player1=1
"""Player 1=You"""
turn=0
"""The player's turn. First player begins"""
if str(sys.argv[1])=='bot':
    player2=3
elif str(sys.argv[1])=='player':
    player2=2
else:
    print("YOU HAVEN'T SPECIFIED A CORRECT ARGUMENT")
pygame.init()
pygame.display.set_caption('MANCALA')
# done variable is using as flag     
done = 1   
while done:
    if turn==0 and done==1:
        """It's player1's turn"""
        done, boxes, player1, turn=event.events(done, boxes, player1, turn)
        table.table(boxes)
    if turn==1 and done==1:
        """It's player2's turn"""
        done, boxes, player2, turn=event.events(done, boxes, player2, turn)
        table.table(boxes)
    if done==4:
        """Check the winner"""
        table.drawWinner(boxes)
        done, boxes, player1, turn=event.events(done, boxes, player1, turn)
# Quite the execution when clicking on close    
pygame.quit()