#########################################################
## File Name: hangman.py                               ##
## Description: Starter for Hangman project - ICS3U    ##
#########################################################
import pygame
import random

pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

limbs = 0
###박진영###
max_limbs = 4
level = 'easy'
#########

def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(GREEN)
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                               )
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()
    
def randomWord():
    ###################################################
    ## 박진영                                          ##
    ## hard 7글자 이상 파일인 words1.txt 가져와서 리턴         ##
    ## easy, normal 7글자 이하 파일인 words2.txt 가져와서 리턴 ##
    ###################################################
    if level == 'hard':
        file = open('words1.txt')
    else:
        file = open('words2.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)
    return f[i][:-1]
    
    #file = open('words.txt')
    #f = file.readlines()
    #i = random.randrange(0, len(f) - 1)
    #return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


def end(winner=False):
    global limbs
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    redraw_game_window()
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner == True:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    ###박진영###
    select_level()
    #########
    reset()


def reset():
    global limbs
    global guessed
    global buttons
    global word
    ###박진영###
    global max_limbs
    #########
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()
    ###박진영###
    max_limbs = 4 if level == 'easy' else 2
    #########
    
#MAINLINE

###박진영###
def select_level():
    global level
    win.fill(WHITE)
    easy_btn = pygame.Rect(winWidth / 2 - 100, winHeight / 2 - 60, 200, 40)
    normal_btn = pygame.Rect(winWidth / 2 - 100, winHeight / 2, 200, 40)
    hard_btn = pygame.Rect(winWidth / 2 - 100, winHeight / 2 + 60, 200, 40)

    pygame.draw.rect(win, BLACK, easy_btn)
    pygame.draw.rect(win, BLACK, normal_btn)
    pygame.draw.rect(win, BLACK, hard_btn)

    easy_label = btn_font.render("Easy", 1, WHITE)
    normal_label = btn_font.render("Normal", 1, WHITE)
    hard_label = btn_font.render("Hard", 1, WHITE)

    win.blit(easy_label, (winWidth / 2 - easy_label.get_width() / 2, winHeight / 2 - 60 + (40 - easy_label.get_height()) / 2))
    win.blit(normal_label, (winWidth / 2 - normal_label.get_width() / 2, winHeight / 2 + (40 - normal_label.get_height()) / 2))
    win.blit(hard_label, (winWidth / 2 - hard_label.get_width() / 2, winHeight / 2 + 60 + (40 - hard_label.get_height()) / 2))

    pygame.display.update()

    selecting = True
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                if easy_btn.collidepoint(clickPos):
                    level = 'easy'
                    selecting = False
                elif normal_btn.collidepoint(clickPos):
                    level = 'normal'
                    selecting = False
                elif hard_btn.collidepoint(clickPos):
                    level = 'hard'
                    selecting = False
#########

# Setup buttons
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
    #buttons.append([color, x_pos, y_pos, radius, visible, char])

###박진영###
select_level()
reset()
#########

#word = randomWord()
inPlay = True

while inPlay:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter != None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    ###박진영###
                    if limbs != 4:
                    #########
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!
