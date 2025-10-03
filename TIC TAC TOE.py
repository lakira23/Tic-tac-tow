import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from pygame.locals import *
import random
import time


pygame.init()

#WINDOW SCALE
window_width = 600
window_height = 600

window = pygame.display.set_mode((window_width, window_height))#settin the display
pygame.display.set_caption('TIC TAC TOE')#title

#background/pictures

grid = pygame.image.load("Grid.png")
O = pygame.image.load("O.png")
X = pygame.image.load("X.png")
menu = pygame.image.load("Menu.png")
error_indication = pygame.image.load("Error_indication.png")

won = pygame.image.load("won.png")
draw = pygame.image.load("draw.png")
#menu
menu_apperance = True

#mouse
clicking = False

clock = pygame.time.Clock()
FPS = 20
def quitgame():
    #quit
    pygame.quit()
    sys.exit()

#non py game
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
runs = 0

x_wins = 0
o_wins = 0

#player_one = str(input("First player's name >> "))
#player_two = str(input("Second person's name >> "))


def draw_outcome(outcome, which):
    if outcome == "draw":
        window.blit(draw,(0,0))
    else:
        window.blit(won,(0,0))


def draw_text(text,font,text_colour,x,y):
    """draw the actual text"""
    img = font.render(text,True,text_colour)
    window.blit(img,(x,y))

def write_text(sentence):
    """write in teh screen"""
    draw_text(sentence,(pygame.font.SysFont("Arial",20)),(255,255,255),150,140)

def win_prop(board):
    # if draw_checker(board) == True:
    #     return "draw"
    # else:
        if runs >= 8:
            return "draw"
        
        if_won = False
        boxes_clock_x = 0
        boxes_clock_o = 0
        boxes_anticlock = 0
        for each_row in range(3):
            boxes_hori_x = 0
            boxes_hori_o = 0
            boxes_verti_x = 0
            boxes_verti_o = 0

            for each_box in range(3):
                if (board[each_box][each_row] == "x"):
                    boxes_hori_x += 1
                if (board[each_box][each_row] == "o"):
                    boxes_hori_o += 1
                if (board[each_row][each_box] == "x"):
                    boxes_verti_x += 1
                if (board[each_row][each_box] == "o"):
                    boxes_verti_o += 1
                    
            if board[each_row][each_row] == "x":
                boxes_clock_x += 1
            if board[each_row][each_row] == "o":
                boxes_clock_o += 1
                    
            if boxes_hori_x == 3 or boxes_verti_x == 3 or boxes_clock_x == 3:
                if_won = True
                return "won"
            
            if boxes_hori_o == 3 or boxes_verti_o == 3 or boxes_clock_o == 3:
                if_won = True
                return "won"
            
        
        if (board[2][0] == "x" and board[1][1] == "x" and board[0][2] == "x") or (board[2][0] == "o" and board[1][1] == "o" and board[0][2] == "o"):
            return "won"

def flashing(x,y):
    x,y = (x//200)*200,(y//200)*200
    window.blit(error_indication,(x+11,y+11))
    pygame.display.update()
    pygame.time.delay(500)
    
def outcome(outcome,winner):
    window.fill((0,0,0))

    if outcome == "draw":
        window.blit(draw,(0,0))
    else:
        if winner == "x":
            window.blit(won,(0,0))
            window.blit(X,((window_width//2) - (X.get_width()/2),(window_height//2) - (X.get_height()/2)))
        else:
            window.blit(won,(0,0))
            window.blit(O,((window_width//2) - (O.get_width()/2),(window_height//2) - (O.get_height()/2)))
    
    pygame.display.update()
    pygame.time.delay(1500)

def draw_players():
    for row in range(3):
        for box in range(3):
            if row >= 200:
                row = int(row /200)
            
            player = board[row][box]    

            if player == " ":
                continue
            
            decider = X if player == "x" else O
            row *= 200
            box *= 200
            coordinates = (row, box)

            window.blit(decider, (coordinates[0]+11,coordinates[1]+11))

def x_grid_position(a,b):
    a_pos = a//200
    b_pos = b//200
    if board[a_pos][b_pos] == " ":
        board[a_pos][b_pos] = "x"
        return True
    else:
        print("space already taken")
        return False

def O_grid_position(a,b):
    a_pos = a//200
    b_pos = b//200
    if board[a_pos][b_pos] == " ":
        board[a_pos][b_pos] = "o"
        return True
    else:
        print("space already taken")
        return False


def x_pick():
    #print("please click where u want x >> ")
    if clicking == True:
        input_taken = x_grid_position(location_mouse[0],location_mouse[1])
        return input_taken

def o_pick():
    #print("please click where u want O >> ")
    if clicking == True:
        input_taken = O_grid_position(location_mouse[0],location_mouse[1])
        return input_taken
        

player = "x"
player_num = 1

game_runner = True

while game_runner:
    clock.tick(FPS)
    print(board)
    input_taken = False
    clicking = False
    finished = False
    
    for event in GAME_EVENTS.get(): ##enables teh ability to exit when needed
        #runs = False
        if event.type == GAME_GLOBALS.QUIT:
            quitgame()

        if event.type == KEYDOWN: ##esc button
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 : ##right click
                clicking = True
                if menu_apperance == False:
                    if player == "x":
                        input_taken = x_pick()
                        if input_taken == False:
                            finished = False

    
                        else:
                            finished = True
                    else:
                        input_taken = o_pick()
                        if input_taken == False:
                            finished = False
                        else:
                            finished = True
                            
                    if finished == False:
                        flashing(location_mouse[0],location_mouse[1])
                    
                    if win_prop(board) == "draw":
                        outcome("draw","-")

                        menu_apperance = True
                        current_apperance = grid
                        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                        runs = 0



                    if win_prop(board) == "won":
                        outcome("won",player)
                        
                        if player == "x":
                            x_wins += 1
                        else:
                            o_wins += 1

                        #game_runner = False
                        menu_apperance = True
                        current_apperance = grid
                        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                        runs = 0
                        
                    #alteranting players
                    runs += 1
                    if player_num == 1 and finished == True:
                        player = "0"
                        player_num = 2
                        ##runs = True
                    elif player_num == 2 and finished == True:
                        player = "x"
                        player_num = 1
                        ##runs = True

    mx,my = pygame.mouse.get_pos()
    location_mouse = [mx,my]
    
    window.fill((0, 0, 0)) ##creates a canvas
    
    if menu_apperance == True:
        current_apperance = menu

        if clicking == True and location_mouse[0] > 144 and location_mouse[0] < 433 and location_mouse[1] > 155 and location_mouse[1] < 211:
            menu_apperance = False
            current_apperance = grid
    
    window.blit(current_apperance, (0, 0))##import the backgroup to the canvas
    if current_apperance == menu:
        draw_text(f"X wins: {x_wins}  O wins: {o_wins}", (pygame.font.SysFont("Arial",20)),(255,5,5),220,320)
    
    if current_apperance == grid:
        draw_players()
    
    

    #checking for clicks
    
    pygame.display.update()##refresh the canvas to present the changes

    

          

