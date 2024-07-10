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
lost_font = pygame.font.SysFont('arial', 20)
title_font = pygame.font.SysFont('arial', 60)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

limbs = 0

##########################
## 김미리
## 힌트 버튼 추가, 힌트 사용 횟수 제한
hint_button = {'color': LIGHT_BLUE, 'x' : winWidth - 100, 'y' : winHeight - 70, 'width' : 80, 'height' : 40, 'text' : 'HINT'}
hint_limit = 3
hint_used = 0
##########################

##########################영진
#def show_page():

######################
def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(WHITE)
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))

    ##########################
    ## 김미리
    ## 힌트 버튼과 남은 힌트 횟수 표시
    pygame.draw.rect(win, hint_button['color'],
                     (hint_button['x'], hint_button['y'], hint_button['width'], hint_button['height']))
    hint_label = btn_font.render(hint_button['text'], 1, BLACK)
    win.blit(hint_label, (hint_button['x'] + (hint_button['width'] - hint_label.get_width()) / 2,
                          hint_button['y'] + (hint_button['height'] - hint_label.get_height()) / 2))

    hint_count_label = btn_font.render(f'{hint_used}/{hint_limit}', 1, BLACK)
    win.blit(hint_count_label, (hint_button['x'] + (hint_button['width'] - hint_count_label.get_width()) / 2,
                                hint_button['y'] + hint_button['height']))
    ##########################

    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


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
    win.fill(WHITE)

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
    reset()


def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()

##########################
## 김미리
## 모든 알파벳 집합, 현재 단어에 사용된 알파벳 집합 생성
## 사용되지 않은 알파벳 리스트 생성
## 사용되지 않은 알파벳이 있을 경우, 무작위로 하나 선택 후 buttons 리스트에서 해당 알파벳 비활성화
def give_hint():
    global buttons, word
    global hint_used

    if hint_used >= hint_limit:
        return
    hint_used += 1

    alphabet = set(chr(i) for i in range(65, 91))
    used_letters = set(word.upper())
    unused_letters = list(alphabet - used_letters - set(guessed))

    if unused_letters:
        hint_letter = random.choice(unused_letters)
        for i in range(len(buttons)):
            if chr(buttons[i][5]) == hint_letter:
                buttons[i][4] = False
                break
##########################

def main_menu():
    menu = True
    while menu:
        win.fill(WHITE)
        title = title_font.render("HANGMAN GAME", 1, BLACK)
        win.blit(title, (winWidth / 2 - title.get_width() / 2, 100))

        easy_button = pygame.Rect(winWidth / 2 - 50, 200, 100, 50)
        normal_button = pygame.Rect(winWidth / 2 - 50, 270, 100, 50)
        hard_button = pygame.Rect(winWidth / 2 - 50, 340, 100, 50)

        pygame.draw.rect(win, LIGHT_BLUE, easy_button)
        pygame.draw.rect(win, LIGHT_BLUE, normal_button)
        pygame.draw.rect(win, LIGHT_BLUE, hard_button)

        easy_label = btn_font.render("Easy", 1, BLACK)
        normal_label = btn_font.render("Normal", 1, BLACK)
        hard_label = btn_font.render("Hard", 1, BLACK)

        win.blit(easy_label, (winWidth / 2 - easy_label.get_width() / 2, 215))
        win.blit(normal_label, (winWidth / 2 - normal_label.get_width() / 2, 285))
        win.blit(hard_label, (winWidth / 2 - hard_label.get_width() / 2, 355))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    #set_difficulty('easy')
                    menu = False
                elif normal_button.collidepoint(event.pos):
                    #set_difficulty('normal')
                    menu = False
                elif hard_button.collidepoint(event.pos):
                    #set_difficulty("hard")
                    menu = False
            ##########################
            ## 김미리
            ## 힌트 버튼 클릭시 give_hint() 함수 호출
            elif (hint_button['x'] < pygame.mouse.get_pos()[0] < hint_button['x'] + hint_button['width'] and hint_button['y'] < pygame.mouse.get_pos()[1] < hint_button['y'] + hint_button['height']):
                give_hint()
            ##########################
        pygame.display.update()



#MAINLINE


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
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

#word = randomWord()
inPlay = True

main_menu()

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
                    if limbs != 5:
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!
