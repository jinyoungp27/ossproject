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
LIGHT_BLUE = (224,224,224)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24, bold=True)
lost_font = pygame.font.SysFont('arial', 20)
title_font = pygame.font.SysFont('arial', 60)
word = ''
buttons = []
guessed = []
level = "easy"
hangmanPics = [pygame.image.load('m_hangman0.png'), pygame.image.load('m_hangman1.png'), pygame.image.load('m_hangman2.png'), pygame.image.load('m_hangman3.png'), pygame.image.load('m_hangman4.png'), pygame.image.load('m_hangman5.png')]




limbs = 0
max_limbs = 5

hint_button = {'color': LIGHT_BLUE, 'x' : winWidth - 100, 'y' : winHeight - 70, 'width' : 80, 'height' : 40, 'text' : 'HINT'}
hint_limit = 3
hint_used = 0

#def show_page():

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

    
    ######이유진####################
    ##글자 및 목숨 이미지 위치 수정 ##
    ################################

    if level == "easy":
        pic = hangmanPics[limbs]
        win.blit(pic, (75, 125))
    else:
        if limbs == 0:
            pic_index = 0 
        elif limbs == 1:
            pic_index = 2
        elif limbs == 2:
            pic_index = 3
        else:
            pic_index = 5
        
        pic = hangmanPics[pic_index]
        win.blit(pic, (75, 125))

    
    word_x = (winWidth - length) // 2
    win.blit(label1,(word_x, 415))

    
    pygame.draw.rect(win, hint_button['color'],
                     (hint_button['x'], hint_button['y'], hint_button['width'], hint_button['height']))
    hint_label = btn_font.render(hint_button['text'], 1, BLACK)
    win.blit(hint_label, (hint_button['x'] + (hint_button['width'] - hint_label.get_width()) / 2,
                          hint_button['y'] + (hint_button['height'] - hint_label.get_height()) / 2))

    hint_count_label = btn_font.render(f'{hint_used}/{hint_limit}', 1, BLACK)
    win.blit(hint_count_label, (hint_button['x'] + (hint_button['width'] - hint_count_label.get_width()) / 2,
                                hint_button['y'] + hint_button['height']))

    
    pygame.display.update()


    
def randomWord():
    global max_limbs
    ###################################################
    ## 박진영                                          ##
    ## hard 7글자 이상 파일인 words1.txt 가져와서 리턴         ##
    ## easy, normal 7글자 이하 파일인 words2.txt 가져와서 리턴 ##
    ###################################################
    if level == 'hard':
        file = open('words_hard.txt')
        max_limbs = 2
    else:
        file = open('words_7.txt')
        if level == "normal":
            max_limbs = 2
        else:
            max_limbs = 4
        
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
    main_menu()
    


def reset():
    global limbs
    global guessed
    global buttons
    global word
    global max_limbs
    global level
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()
    max_limbs = 5

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
   
#이영진
#난이도 선택을 위한 시작화면 설계
def main_menu():
    global menu
    menu = True
    global level
    global word

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
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    level = "easy"
                    word = randomWord()
                    menu = False
                elif normal_button.collidepoint(event.pos):
                    level = "normal"
                    word = randomWord()
                    menu = False
                elif hard_button.collidepoint(event.pos):
                    level = "hard"
                    word = randomWord()
                    menu = False
        
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

    
    ##이유진 ########################
    ##알파벳 버튼 UI 수정##

    buttons.append([WHITE, x, y, 0, True, 65 + i])
    
    #buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
    #buttons.append([color, x_pos, y_pos, radius, visible, char])


word = randomWord()
reset()
main_menu()


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
                    if limbs < max_limbs:
                        limbs += 1
                    else:
                        limbs += 1
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)
            ## 김미리
            ## 힌트 버튼 클릭시 give_hint() 함수 호출
            if (hint_button['x'] < pygame.mouse.get_pos()[0] < hint_button['x'] + hint_button['width'] and hint_button['y'] < pygame.mouse.get_pos()[1] < hint_button['y'] + hint_button['height']):
                            give_hint()

pygame.quit()

# always quit pygame when done!
