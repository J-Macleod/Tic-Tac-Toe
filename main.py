# Tic Tac Toe
# by Jacob Macleod
# Started in 2020
# Updated in 2022

import pygame
import os

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()
pygame.mixer.init()

icon = pygame.image.load("images/icon.png")

display_width = 450
display_height = 430
fps = 75

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.display.set_icon(icon)
pygame.display.set_caption("Tic Tac Toe")
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

the_font = "font/OpenSans-Regular.ttf"

black = (0, 0, 0)
red = (250, 10, 10)
green = (10, 250, 10)
blue = (10, 10, 250)
white = (255, 255, 255)

def box_text(text, size, x, y, font, color):
    loading_text = pygame.font.Font(font, size)

    TextSurf, TextRect = text_objects(text, loading_text, color)
    TextRect.midleft = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def center_text(text, size, x, y, font, color):
    loading_text = pygame.font.Font(font, size)

    TextSurf, TextRect = text_objects(text, loading_text, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def display_image(image,x,y):
    gameDisplay.blit(image, (x,y))

screen_mode = 1

def screen_switch():
    global screen_mode
    if screen_mode == 1:
        gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
        screen_mode = 2
    elif screen_mode == 2:
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        screen_mode = 1

def main():
    up = True

    ximg = pygame.image.load("images/x.png")
    oimg = pygame.image.load("images/o.png")

    turn = "X"

    col1row1 = None
    col1row2 = None
    col1row3 = None

    col2row1 = None
    col2row2 = None
    col2row3 = None

    col3row1 = None
    col3row2 = None
    col3row3 = None

    xwins = False
    owins = False
    nowins = False

    while up:

        mouse_pos = pygame.mouse.get_pos()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 or event.key == pygame.K_ESCAPE:
                    screen_switch()
                elif event.key == pygame.K_r:
                    turn = "X"

                    col1row1 = None
                    col1row2 = None
                    col1row3 = None

                    col2row1 = None
                    col2row2 = None
                    col2row3 = None

                    col3row1 = None
                    col3row2 = None
                    col3row3 = None

                    xwins = False
                    owins = False
                    nowins = False
            if event.type == pygame.MOUSEBUTTONUP:
                if xwins == False and owins == False:
                    #col 1
                    if 75 <= mouse_pos[0] <= 175 and 50 <= mouse_pos[1] <= 150: 
                        if col1row1 == None:
                            col1row1 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 75 <= mouse_pos[0] <= 175 and 150 <= mouse_pos[1] <= 250: 
                        if col1row2 == None:
                            col1row2 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 75 <= mouse_pos[0] <= 175 and 250 <= mouse_pos[1] <= 350: 
                        if col1row3 == None:
                            col1row3 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    #col 2
                    elif 175 <= mouse_pos[0] <= 275 and 50 <= mouse_pos[1] <= 150: 
                        if col2row1 == None:
                            col2row1 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 175 <= mouse_pos[0] <= 275 and 150 <= mouse_pos[1] <= 250: 
                        if col2row2 == None:
                            col2row2 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 175 <= mouse_pos[0] <= 275 and 250 <= mouse_pos[1] <= 350: 
                        if col2row3 == None:
                            col2row3 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    #col 3
                    elif 275 <= mouse_pos[0] <= 375 and 50 <= mouse_pos[1] <= 150: 
                        if col3row1 == None:
                            col3row1 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 275 <= mouse_pos[0] <= 375 and 150 <= mouse_pos[1] <= 250: 
                        if col3row2 == None:
                            col3row2 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                    elif 275 <= mouse_pos[0] <= 375 and 250 <= mouse_pos[1] <= 350: 
                        if col3row3 == None:
                            col3row3 = turn
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                
        gameDisplay.fill(white)
        
        #pygame.draw.rect(gameDisplay, blue, (75,50,300,300))
        pygame.draw.rect(gameDisplay, black, (75,150,300,5))
        pygame.draw.rect(gameDisplay, black, (75,250,300,5))
        pygame.draw.rect(gameDisplay, black, (175,50,5,300))
        pygame.draw.rect(gameDisplay, black, (275,50,5,300))

        #col 1
        if col1row1 == None:
            pass
        elif col1row1 == "X":
            display_image(ximg, 75, 50)
        elif col1row1 == "O":
            display_image(oimg, 75, 50)

        if col1row2 == None:
            pass
        elif col1row2 == "X":
            display_image(ximg, 75, 150)
        elif col1row2 == "O":
            display_image(oimg, 75, 150)

        if col1row3 == None:
            pass
        elif col1row3 == "X":
            display_image(ximg, 75, 250)
        elif col1row3 == "O":
            display_image(oimg, 75, 250)

        #col 2
        if col2row1 == None:
            pass
        elif col2row1 == "X":
            display_image(ximg, 175, 50)
        elif col2row1 == "O":
            display_image(oimg, 175, 50)

        if col2row2 == None:
            pass
        elif col2row2 == "X":
            display_image(ximg, 175, 150)
        elif col2row2 == "O":
            display_image(oimg, 175, 150)

        if col2row3 == None:
            pass
        elif col2row3 == "X":
            display_image(ximg, 175, 250)
        elif col2row3 == "O":
            display_image(oimg, 175, 250)
        
        #col 3
        if col3row1 == None:
            pass
        elif col3row1 == "X":
            display_image(ximg, 275, 50)
        elif col3row1 == "O":
            display_image(oimg, 275, 50)

        if col3row2 == None:
            pass
        elif col3row2 == "X":
            display_image(ximg, 275, 150)
        elif col3row2 == "O":
            display_image(oimg, 275, 150)

        if col3row3 == None:
            pass
        elif col3row3 == "X":
            display_image(ximg, 275, 250)
        elif col3row3 == "O":
            display_image(oimg, 275, 250)
        
        if xwins == False and owins == False and nowins == False:
            center_text("Turn: " + turn, 20, display_width / 2, display_height - 30, the_font, black)

        # Col 1 Match
        if col1row1 == "X" and col1row1 == col1row2 and col1row2 == col1row3:
            xwins = True
        elif col1row1 == "O" and col1row1 == col1row2 and col1row2 == col1row3:
            owins = True

        # Col 2 Match
        elif col2row1 == "X" and col2row1 == col2row2 and col2row2 == col2row3:
            xwins = True
        elif col2row1 == "O" and col2row1 == col2row2 and col2row2 == col2row3:
            owins = True

        # Col 3 Match
        elif col3row1 == "X" and col3row1 == col3row2 and col3row2 == col3row3:
            xwins = True
        elif col3row1 == "O" and col3row1 == col3row2 and col3row2 == col3row3:
            owins = True

        # Row 1 Match
        elif col1row1 == "X" and col1row1 == col2row1 and col2row1 == col3row1:
            xwins = True
        elif col1row1 == "O" and col1row1 == col2row1 and col2row1 == col3row1:
            owins = True

        # Row 2 Match
        elif col1row2 == "X" and col1row2 == col2row2 and col2row2 == col3row2:
            xwins = True
        elif col1row2 == "O" and col1row2 == col2row2 and col2row2 == col3row2:
            owins = True

        # Row 3 Match
        elif col1row3 == "X" and col1row3 == col2row3 and col2row3 == col3row3:
            xwins = True
        elif col1row3 == "O" and col1row3 == col2row3 and col2row3 == col3row3:
            owins = True

        # Diagonal \
        elif col1row1 == "X" and col1row1 == col2row2 and col1row1 == col3row3:
            xwins = True
        elif col1row1 == "O" and col1row1 == col2row2 and col1row1 == col3row3:
            owins = True

        # Diagonal /
        elif col1row3 == "X" and col1row3 == col2row2 and col1row3 == col3row1:
            xwins = True
        elif col1row3 == "O" and col1row3 == col2row2 and col1row3 == col3row1:
            owins = True

        elif col1row1 != None and col1row2 != None and col1row3 != None:
            if col2row1 != None and col2row2 != None and col2row3 != None:
                if col3row1 != None and col3row2 != None and col3row3 != None:
                    nowins = True
            
        # Winner
        if xwins:
            center_text("X Wins", 20, display_width / 2, 20, the_font, black)
            center_text("(Click R to restart)", 10, display_width / 2, 40, the_font, (100,100,100))
        elif owins:
            center_text("O Wins", 20, display_width / 2, 20, the_font, black)
            center_text("(Click R to restart)", 10, display_width / 2, 40, the_font, (100,100,100))
        elif nowins:
            center_text("No One Wins", 20, display_width / 2, 20, the_font, black)
            center_text("(Click R to restart)", 10, display_width / 2, 40, the_font, (100,100,100))
        
        pygame.display.update()
        clock.tick(fps)

main()

