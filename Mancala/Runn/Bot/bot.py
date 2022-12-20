import random


def choosemove(boxes):
    """Chooses randomly one to boxes from his side of the board"""
    listmoves=[]
    for box in range(6):
        if boxes[0][box]!=0:
            listmoves.append(box+1)
    if len(listmoves)==1:
        move=listmoves[0]
    else:
        move=random.choice(listmoves)
    print(move, listmoves)
    listmoves.clear()
    return move
