import pygame
import random
from math import inf

listA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def full():
    if ' ' not in listA:
        return True
    return False


def winner(play):
    if play[0] == play[1] == play[2] == 'X' or play[0] == play[3] == play[6] == 'X' \
            or play[0] == play[4] == play[8] == 'X' or play[4] == play[1] == play[7] == 'X' \
            or play[4] == play[2] == play[6] == 'X' or play[4] == play[3] == play[5] == 'X' \
            or play[8] == play[5] == play[2] == 'X' or play[8] == play[7] == play[6] == 'X':
        return 'X'
    elif play[0] == play[1] == play[2] == 'O' or play[0] == play[3] == play[6] == 'O' \
            or play[0] == play[4] == play[8] == 'O' or play[4] == play[1] == play[7] == 'O' \
            or play[4] == play[2] == play[6] == 'O' or play[4] == play[3] == play[5] == 'O' \
            or play[8] == play[5] == play[2] == 'O' or play[8] == play[7] == play[6] == 'O':
        return 'O'
    return False


def minimax(board, depth, isMax):
    if winner(listA) == 'O':
        return 10 - depth
    elif winner(listA) == 'X':
        return -10 + depth
    elif full():
        return 0

    listAvail = []
    # create list of available spots
    for i in range(len(listA)):
        if listA[i] == ' ':
            listAvail.append(i)
    if isMax:
        bestScore = -inf
        for i in listAvail:
            listA[i] = 'O'
            score = minimax(board, depth + 1, False)
            listA[i] = ' '
            bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = inf
        for i in listAvail:
            listA[i] = 'X'
            score = minimax(board, depth + 1, True)
            listA[i] = ' '
            bestScore = min(bestScore, score)
        return bestScore


def compChoice():
    listAvail = []
    # create list of available spots
    for i in range(len(listA)):
        if listA[i] == ' ':
            listAvail.append(i)
    bestScore = -inf
    move = -1
    maybe = [move]
    for i in listAvail:
        listA[i] = 'O'
        score = minimax(listA, 0, False)
        listA[i] = ' '
        if score == bestScore:
            maybe.append(i)
        elif score > bestScore:
            bestScore = score
            move = i
            maybe = [move]
    print(maybe)
    return random.choice(maybe)


# Initializes PyGame
pygame.init()

# Creates a window for game
win = pygame.display.set_mode((550, 550))

# Sets the title of window
pygame.display.set_caption('PyGame Tic-Tac-Toe')

pygame.draw.rect(win, (255, 255, 255), (0, 0, 550, 550))

# Draws the game board
one = pygame.draw.rect(win, (0, 0, 0), (25, 25, 150, 150))
two = pygame.draw.rect(win, (0, 0, 0), (200, 25, 150, 150))
three = pygame.draw.rect(win, (0, 0, 0), (375, 25, 150, 150))
four = pygame.draw.rect(win, (0, 0, 0), (25, 200, 150, 150))
five = pygame.draw.rect(win, (0, 0, 0), (200, 200, 150, 150))
six = pygame.draw.rect(win, (0, 0, 0), (375, 200, 150, 150))
seven = pygame.draw.rect(win, (0, 0, 0), (25, 375, 150, 150))
eight = pygame.draw.rect(win, (0, 0, 0), (200, 375, 150, 150))
nine = pygame.draw.rect(win, (0, 0, 0), (375, 375, 150, 150))

# Main Loop
run = True
oneOpen = True
twoOpen = True
threeOpen = True
fourOpen = True
fiveOpen = True
sixOpen = True
sevenOpen = True
eightOpen = True
nineOpen = True

compTurn = False

while run:

    # Refresh Time
    pygame.time.delay(20)

    # Pygame Events
    if not compTurn:
        for event in pygame.event.get():

            # Quit Event
            if event.type == pygame.QUIT:
                run = False

            # Space bar to reset
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    listA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    oneOpen = True
                    twoOpen = True
                    threeOpen = True
                    fourOpen = True
                    fiveOpen = True
                    sixOpen = True
                    sevenOpen = True
                    eightOpen = True
                    nineOpen = True
                    compTurn = False
                    one = pygame.draw.rect(win, (0, 0, 0), (25, 25, 150, 150))
                    two = pygame.draw.rect(win, (0, 0, 0), (200, 25, 150, 150))
                    three = pygame.draw.rect(win, (0, 0, 0), (375, 25, 150, 150))
                    four = pygame.draw.rect(win, (0, 0, 0), (25, 200, 150, 150))
                    five = pygame.draw.rect(win, (0, 0, 0), (200, 200, 150, 150))
                    six = pygame.draw.rect(win, (0, 0, 0), (375, 200, 150, 150))
                    seven = pygame.draw.rect(win, (0, 0, 0), (25, 375, 150, 150))
                    eight = pygame.draw.rect(win, (0, 0, 0), (200, 375, 150, 150))
                    nine = pygame.draw.rect(win, (0, 0, 0), (375, 375, 150, 150))

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if one.collidepoint(pos) and oneOpen:
                    pygame.draw.line(win, (255, 255, 255), (45, 40), (155, 160), 25)
                    pygame.draw.line(win, (255, 255, 255), (155, 40), (45, 160), 25)
                    listA[0] = 'X'
                    oneOpen = False
                    compTurn = True

                if two.collidepoint(pos) and twoOpen:
                    pygame.draw.line(win, (255, 255, 255), (220, 40), (330, 160), 25)
                    pygame.draw.line(win, (255, 255, 255), (330, 40), (220, 160), 25)
                    listA[1] = 'X'
                    twoOpen = False
                    compTurn = True

                if three.collidepoint(pos) and threeOpen:
                    pygame.draw.line(win, (255, 255, 255), (395, 40), (505, 160), 25)
                    pygame.draw.line(win, (255, 255, 255), (505, 40), (395, 160), 25)
                    listA[2] = 'X'
                    threeOpen = False
                    compTurn = True

                if four.collidepoint(pos) and fourOpen:
                    pygame.draw.line(win, (255, 255, 255), (45, 215), (155, 335), 25)
                    pygame.draw.line(win, (255, 255, 255), (155, 215), (45, 335), 25)
                    listA[3] = 'X'
                    fourOpen = False
                    compTurn = True

                if five.collidepoint(pos) and fiveOpen:
                    pygame.draw.line(win, (255, 255, 255), (220, 215), (330, 335), 25)
                    pygame.draw.line(win, (255, 255, 255), (330, 215), (220, 335), 25)
                    listA[4] = 'X'
                    fiveOpen = False
                    compTurn = True

                if six.collidepoint(pos) and sixOpen:
                    pygame.draw.line(win, (255, 255, 255), (395, 215), (505, 335), 25)
                    pygame.draw.line(win, (255, 255, 255), (505, 215), (395, 335), 25)
                    listA[5] = 'X'
                    sixOpen = False
                    compTurn = True

                if seven.collidepoint(pos) and sevenOpen:
                    pygame.draw.line(win, (255, 255, 255), (45, 390), (155, 510), 25)
                    pygame.draw.line(win, (255, 255, 255), (155, 390), (45, 510), 25)
                    listA[6] = 'X'
                    sevenOpen = False
                    compTurn = True

                if eight.collidepoint(pos) and eightOpen:
                    pygame.draw.line(win, (255, 255, 255), (220, 390), (330, 510), 25)
                    pygame.draw.line(win, (255, 255, 255), (330, 390), (220, 510), 25)
                    listA[7] = 'X'
                    eightOpen = False
                    compTurn = True

                if nine.collidepoint(pos) and nineOpen:
                    pygame.draw.line(win, (255, 255, 255), (395, 390), (505, 510), 25)
                    pygame.draw.line(win, (255, 255, 255), (505, 390), (395, 510), 25)
                    listA[8] = 'X'
                    nineOpen = False
                    compTurn = True

    pygame.display.update()

    if winner(listA):
        compTurn = False
        oneOpen = False
        twoOpen = False
        threeOpen = False
        fourOpen = False
        fiveOpen = False
        sixOpen = False
        sevenOpen = False
        eightOpen = False
        nineOpen = False

    if compTurn:
        comp = compChoice()
        if comp == 0:
            pygame.draw.circle(win, (255, 255, 255), (100, 100), 60, 15)
            listA[0] = 'O'
            oneOpen = False

        elif comp == 1:
            pygame.draw.circle(win, (255, 255, 255), (275, 100), 60, 15)
            listA[1] = 'O'
            twoOpen = False

        elif comp == 2:
            pygame.draw.circle(win, (255, 255, 255), (450, 100), 60, 15)
            listA[2] = 'O'
            threeOpen = False

        elif comp == 3:
            pygame.draw.circle(win, (255, 255, 255), (100, 275), 60, 15)
            listA[3] = 'O'
            fourOpen = False

        elif comp == 4:
            pygame.draw.circle(win, (255, 255, 255), (275, 275), 60, 15)
            listA[4] = 'O'
            fiveOpen = False

        elif comp == 5:
            pygame.draw.circle(win, (255, 255, 255), (450, 275), 60, 15)
            listA[5] = 'O'
            sixOpen = False

        elif comp == 6:
            pygame.draw.circle(win, (255, 255, 255), (100, 450), 60, 15)
            listA[6] = 'O'
            sevenOpen = False

        elif comp == 7:
            pygame.draw.circle(win, (255, 255, 255), (275, 450), 60, 15)
            listA[7] = 'O'
            eightOpen = False

        elif comp == 8:
            pygame.draw.circle(win, (255, 255, 255), (450, 450), 60, 15)
            listA[8] = 'O'
            nineOpen = False

    compTurn = False
    pygame.display.update()

pygame.quit()
