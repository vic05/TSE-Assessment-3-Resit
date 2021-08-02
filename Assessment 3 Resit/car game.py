#Importing and initialising libraries
import pygame #Imports the library
pygame.init()
pygame.font.init()
import time
import random

#SQLite
import sqlite3
con = sqlite3.connect('score.db') #Establishes connection with database
cur = con.cursor() #Defines cursor variable

#Pre-defined variables
which_subroutine = 'mainMenu' #Sets the initial subroutine to main menu
window_size = [550, 685] #Stores the width and height of the window
white = [255, 255, 255] #Defines white colour using RGB numbers
black = [0, 0, 0] #Defines black colour using RGB numbers
blue = [0, 120, 255] #Defines the blue colour using RGB numbers
light_blue = [7, 180, 255] #Defines the light blue colour using RGB numbers
green = [42, 224, 78] #Defines the green colour using RGB numbers
red = [255, 0, 0] #Defines the red colour using RGB numbers
clock = pygame.time.Clock() #Prepares variable which can be used to chnage the frames per second
instructions_text_file = open('Instructions.txt', 'r') #Variable storing contents of text file
instructions_text_array = instructions_text_file.read().splitlines() #Splits text into separate lines and stores in array
instructions_text_file.close() #Closes file

pygame.display.set_caption("Car Game") #Sets the name of the window
screen = pygame.display.set_mode(window_size) #Creates the window

#Normal python / pygame subroutines

def main_menu(): #Main menu subroutine
    screen.fill(white) #Makes background white
    title_font = pygame.font.SysFont('Calibri', 30) #Sets preferred font and size
    button_font = pygame.font.SysFont('Calibri', 25) #Sets preferred font and size
    main_menu_text = title_font.render('Main Menu', True, (black))
    screen.blit(main_menu_text, (205, 30)) #This and the command above display 'Main Menu'
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos() #Gets the mouse position on the screen and stores it in the array
    global which_subroutine #Declares the variable as global so that it works outside of the subroutine
    if 150+250 > mouse_position[0] > 150 and 100+50 > mouse_position[1] > 100:
        pygame.draw.rect(screen, light_blue, (150, 100, 250, 50))
        button_text_1 = button_font.render('Start Game', True, (black))
        screen.blit(button_text_1, (220, 113)) #This and the command above display 'Start Game'
        if mouse_pressed[0] == 1: #Detects when mouse button is pressed
            which_subroutine = 'mainGameSubroutine' #Sets variable to 'instructionScreen' to run subroutine
    else:
        pygame.draw.rect(screen, blue, (150, 100, 250, 50))
        button_text_1 = button_font.render('Start Game', True, (black))
        screen.blit(button_text_1, (220, 113)) #This and the command above display 'Start Game'
    if 150+250 > mouse_position[0] > 150 and 200+50 > mouse_position[1] > 200:
        pygame.draw.rect(screen, light_blue, (150, 200, 250, 50))
        button_text_2 = button_font.render('Instructions', True, (black))
        screen.blit(button_text_2, (220, 213)) #This and the command above display 'Instructions'
        if mouse_pressed[0] == 1: #Detects when mouse button is pressed
            which_subroutine = 'instructionScreen' #Sets variable to 'instructionScreen' to run instructions subroutine
    else:
        pygame.draw.rect(screen, blue, (150, 200, 250, 50))
        button_text_2 = button_font.render('Instructions', True, (black))
        screen.blit(button_text_2, (220, 213)) #This and the command above display 'Instructions'
    if 150+250 > mouse_position[0] > 150 and 300+50 > mouse_position[1] > 300:
        pygame.draw.rect(screen, light_blue, (150, 300, 250, 50))
        button_text_3 = button_font.render('Leader-board', True, (black))
        screen.blit(button_text_3, (210, 313)) #This and the command above display 'Leader-board'
        if mouse_pressed[0] == 1:
            which_subroutine = 'leaderBoard'
    else:
        pygame.draw.rect(screen, blue, (150, 300, 250, 50))
        button_text_3 = button_font.render('Leader-board', True, (black))
        screen.blit(button_text_3, (210, 313)) #This and the command above display 'Leader-board'
    #The commands above monitor the mouse position and if the mouse position is within the parameters of...
    #...the rectangular button the colour will change to a slightly lighter blue to shows that the program recognises...
    #...the position of the mouse.


def instruction_screen(): #Instruction screen subroutine
    screen.fill(white) #Clears the previous screen by making the screen white again
    title_font = pygame.font.SysFont('Calibri', 50) #Sets preferred font and size
    instruction_screen_title_text = title_font.render('Instructions', True, (black))
    screen.blit(instruction_screen_title_text, (155, 20)) #This and the line above display 'Instructions' title
    instructions_font = pygame.font.SysFont('Calibri', 21) #Sets preferred font and size
    y_coord = 80 #Pre-defines y coordinate
    place_holder = 0 #Sets variable to 0 to use in FOR loop
    for x in instructions_text_array: #FOR loop
        instructions_text = instructions_font.render((instructions_text_array[place_holder]), True, (black))
        screen.blit(instructions_text, (30, y_coord))
        place_holder += 1
        y_coord += 20
        #The above 4 lines of code print the contents of the text file line-by-line, incrementing the y coordinate...
        #...everytime so that the line is displayed below the previous
    button_font = pygame.font.SysFont('Calibri', 25) #Sets preferred font and size
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos() #Gets the mouse position on the screen and stores it in the array
    global which_subroutine #Declares the variable as global so that it works outside of the subroutine
    if 150+250 > mouse_position[0] > 150 and 350+50 > mouse_position[1] > 350:
        pygame.draw.rect(screen, light_blue, (150, 350, 250, 50))
        button_text_1 = button_font.render('Back', True, (black))
        screen.blit(button_text_1, (252, 363)) #This and the command above display 'Back'
        if mouse_pressed[0] == 1:
            which_subroutine = 'mainMenu' #Sets variable to 'mainMenu' to run instructions subroutine
    else:
        pygame.draw.rect(screen, blue, (150, 350, 250, 50))
        button_text_1 = button_font.render('Back', True, (black))
        screen.blit(button_text_1, (252, 363)) #This and the command above display 'Back'


def background():
    background_image = pygame.image.load('background.png') #Loads the background
    screen.blit(background_image, (0,0)) #Displays the background


def player_vehicle(player_coords):
    red_car = pygame.image.load('red_car.png') #Loads the image of the red car
    screen.blit(red_car, (player_coords)) #Displays the image


def other_vehicle(random_lane, start_y):
    blue_car = pygame.image.load('blue_car.png') #Loads the image of the blue car
    screen.blit(blue_car, (random_lane, start_y)) #Displays the image


def main_game_subroutine(player_coords, random_lane, start_y, random_speed):
    background()
    player_vehicle(player_coords)
    other_vehicle(random_lane, start_y)
    start_y += random_speed #Adds value of random speed to y-position with ever repetition of the while loop
    

def title(message):
    font = pygame.font.SysFont('Calibri', 50) #Sets preferred font and size
    text = font.render(message, True, (black))
    text_rect = text.get_rect(center=(window_size[0]/2, 100)) #Centres text
    #Returns Rect object in order to center text on the screen
    screen.blit(text, text_rect) #Displays text


def crash():
    screen.fill(white) #Clears the previous screen by making the screen white again
    title("You Crashed") #Runs subroutine
    button('Save Score', 150, 150)
    button('Play Again', 150, 250)
    button('Main Menu', 150, 350)
    button('Quit', 150, 450)


def button(text, button_x, button_y):
    font = pygame.font.SysFont('Calibri', 25)
    button_text = font.render(text, True, (black))
    mouse_position = pygame.mouse.get_pos() #Gets mouse position
    if button_x + 250 > mouse_position[0] > button_x and button_y + 50 > mouse_position[1] > button_y:
        pygame.draw.rect(screen, light_blue, (button_x, button_y, 250, 50))
        if 8 >= len(text) >= 4: #Displayes shorter words in the centre
            screen.blit(button_text, (250, button_y + 13))
        else:
            screen.blit(button_text, (220, button_y + 13))
    else:
        pygame.draw.rect(screen, blue, (button_x, button_y, 250, 50))
        if 8 >= len(text) >= 4:
            screen.blit(button_text, (250, button_y + 13))
        else:
            screen.blit(button_text, (220, button_y + 13))

    global which_subroutine
    mouse_pressed = pygame.mouse.get_pressed() #Detects if mouse button is pressed
    if 150 + 250 > mouse_position[0] > 150 and 150 + 50 > mouse_position[1] > 150:
        if mouse_pressed[0] == 1:
            which_subroutine = 'saveScore'

    if 150 + 250 > mouse_position[0] > 150 and 250 + 50 > mouse_position[1] > 250:
        if mouse_pressed[0] == 1:
            which_subroutine = 'mainGameSubroutine'
            time.sleep(0.3) #Makes the program sleep
            game_loop() #Runs main game loop

    if 150 + 250 > mouse_position[0] > 150 and 350 + 50 > mouse_position[1] > 350:
        if mouse_pressed[0] == 1:
            which_subroutine = 'mainMenu'
            time.sleep(0.2)
            game_loop()

    if 150 + 250 > mouse_position[0] > 150 and 450 + 50 > mouse_position[1] > 450:
        if mouse_pressed[0] == 1:
            pygame.quit() #Quits game
            quit()

    if 150 + 250 > mouse_position[0] > 150 and 530 + 50 > mouse_position[1] > 530:
        if mouse_pressed[0] == 1:
            which_subroutine = 'clearLeaderboard'
            time.sleep(0.1)
            game_loop()

    if 150 + 250 > mouse_position[0] > 150 and 600 + 50 > mouse_position[1] > 600:
        if mouse_pressed[0] == 1:
            which_subroutine = 'mainMenu'
            time.sleep(0.1)
            game_loop()


def cars_dodged(count):
    font = pygame.font.SysFont('Calibri', 22)
    text = font.render("Dodged: " + str(count), True, (black)) #Displays 'Dodged:' and the number of cars dodged
    screen.blit(text, (405, 10))
            

def save_score(typing):
    screen.fill(white)
    global joined_list
    joined_list = ''.join(typing) #Combines all items in the typing list
    title("Save Score")
    font = pygame.font.SysFont('Calibri', 20)
    text = font.render("Username: " + str(joined_list), True, (black))
    screen.blit(text, (10, 150))
    text_1 = font.render("Press the enter key to confirm.", True, (black))
    screen.blit(text_1, (10, 200))


def clear_leaderboard():
    screen.fill(white)
    font = pygame.font.SysFont('Calibri', 30)
    text = font.render("Press the delete key to confirm.", True, (black))
    screen.blit(text, (75, 50))


#SQLite Subroutines

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS score(playername TEXT, count INTEGER)')
    #Creates the table if it doesn't exist

create_table() #Runs subroutine staright after defining it to check if table exists

def data_entry(count, playername):
    cur.execute('INSERT INTO score (playername, count) VALUES (?, ?)', (playername, count)) #Inserts variables
    con.commit() #Saves changes to the database


def read_from_database():
    screen.fill(white)
    title("Leader Board")
    y = 150
    num = 1
    font = pygame.font.SysFont('Calibri', 25)
    cur.execute('SELECT * FROM score ORDER BY count DESC')
    for row in cur.fetchall(): #Fetches table by rows
        if num <= 10:
            text = font.render(str(num), True, (black)) #Displays order in leader-board
            text_1 = font.render(row[0], True, (red)) #Displays name
            text_2 = font.render( str(row[1]), True, (green)) #Displays score
            screen.blit(text, (20, y))
            screen.blit(text_1, (85, y))
            screen.blit(text_2, (300, y))
            y += 35
            num += 1

    button("Clear", 150, 530) #Creates clear leader-board button
    button("Back", 150, 600) #Creates back button
    


#Main game loop

def game_loop():
    player_coords = [75, 550] #Array in main game subroutine storing coordinates of user's vehicle
    vehicle_height = 70
    start_y = -150 #Starting y-position of the computer-controlled vehicles
    lane = [75, 193.5, 312] #List of the x-positions of the three lanes
    random_lane = random.choice(lane) #Randomly chooses the starting lane
    speed = [30, 35, 40, 40, 42, 45] #List of different speeds that the computer-controlled vehicles can drive at
    random_speed = random.choice(speed) #Randomly chooses starting speed
    global count
    count = 0 #Sets initial score count to 0

    global typing
    typing = [] #Creates list to store characters pressed by the player
    
    global which_subroutine

    done = False

    while not done:
        for event in pygame.event.get(): #Detects if user clicks something
            if event.type == pygame.QUIT: #Detects if user clicks close
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if len(typing) < 15:
                    if event.key == pygame.K_a:
                        typing.append('a') #Adds the corresponding letter to the end of the list
                    if event.key == pygame.K_b:
                        typing.append('b')
                    if event.key == pygame.K_c:
                        typing.append('c')
                    if event.key == pygame.K_d:
                        typing.append('d')
                    if event.key == pygame.K_e:
                        typing.append('e')
                    if event.key == pygame.K_f:
                        typing.append('f')
                    if event.key == pygame.K_g:
                        typing.append('g')
                    if event.key == pygame.K_h:
                        typing.append('h')
                    if event.key == pygame.K_i:
                        typing.append('i')
                    if event.key == pygame.K_j:
                        typing.append('j')
                    if event.key == pygame.K_k:
                        typing.append('k')
                    if event.key == pygame.K_l:
                        typing.append('l')
                    if event.key == pygame.K_m:
                        typing.append('m')
                    if event.key == pygame.K_n:
                        typing.append('n')
                    if event.key == pygame.K_o:
                        typing.append('o')
                    if event.key == pygame.K_p:
                        typing.append('p')
                    if event.key == pygame.K_q:
                        typing.append('q')
                    if event.key == pygame.K_r:
                        typing.append('r')
                    if event.key == pygame.K_s:
                        typing.append('s')
                    if event.key == pygame.K_t:
                        typing.append('t')
                    if event.key == pygame.K_u:
                        typing.append('u')
                    if event.key == pygame.K_v:
                        typing.append('v')
                    if event.key == pygame.K_w:
                        typing.append('w')
                    if event.key == pygame.K_x:
                        typing.append('x')
                    if event.key == pygame.K_y:
                        typing.append('y')
                    if event.key == pygame.K_z:
                        typing.append('z')
                    if event.key == pygame.K_0:
                        typing.append('0')
                    if event.key == pygame.K_1:
                        typing.append('1')
                    if event.key == pygame.K_2:
                        typing.append('2')
                    if event.key == pygame.K_3:
                        typing.append('3')
                    if event.key == pygame.K_4:
                        typing.append('4')
                    if event.key == pygame.K_5:
                        typing.append('5')
                    if event.key == pygame.K_6:
                        typing.append('6')
                    if event.key == pygame.K_7:
                        typing.append('7')
                    if event.key == pygame.K_8:
                        typing.append('8')
                    if event.key == pygame.K_9:
                        typing.append('9')
                    if event.key == pygame.K_SPACE:
                        typing.append(' ')
                    if event.key == pygame.K_PERIOD:
                        typing.append('.')
                    if event.key == pygame.K_UNDERSCORE:
                        typing.append('_')
                    if event.key == pygame.K_MINUS:
                        typing.append('-')
                if event.key == pygame.K_RETURN and len(typing) > 0:
                    screen.fill(white)
                    data_entry(count, joined_list)
                    title("Score Saved!")
                    pygame.display.update()
                    which_subroutine = 'mainMenu'
                    time.sleep(1)
                    game_loop()
                if event.key == pygame.K_DELETE:
                    cur.execute('DELETE FROM score') #Delete all records form the table
                    con.commit()
                    screen.fill(white)
                    title("Leader-board Cleared!")
                    pygame.display.update()
                    which_subroutine = 'mainMenu'
                    time.sleep(1)
                    game_loop()
                if event.key == pygame.K_BACKSPACE:
                    length = len(typing) #Gets length of list
                    if length > 0:
                        del typing[length - 1] #Deletes last value added to the list

                #The lines of code above detect when the player presses any character on the keyboard which are...
                #...in the alphabet as well as some other characters (period, underscore, dash) and also the space...
                #...key, the enter key and the backspace key

                if event.key == pygame.K_LEFT:
                    if 75 < player_coords[0] <= 312: #Runs if player's car is within the boundaries
                        player_coords[0] -= 118.5 #Decrements x-coordinate

                if event.key == pygame.K_RIGHT:
                    if 75 <= player_coords[0] < 312:
                        player_coords[0] += 118.5 #Increments x-coordinate

                #The lines of code above detect when the player presses the left or right key on the keyboard and...
                #...switches lane accordingly by changing the x-coordinate of the vehicle


        if which_subroutine == 'mainMenu':
            main_menu()
        elif which_subroutine == 'instructionScreen':
            instruction_screen()
        elif which_subroutine == 'mainGameSubroutine':
            background()
            cars_dodged(count)
            player_vehicle(player_coords)
            other_vehicle(random_lane, start_y)
            start_y += random_speed #Adds value of random speed to y-position with ever repetition of the while loop
        elif which_subroutine == 'crash':
            crash()
        elif which_subroutine == 'saveScore':
            save_score(typing)
        elif which_subroutine == 'leaderBoard':
            read_from_database()
        elif which_subroutine == 'clearLeaderboard':
            clear_leaderboard()
    #The 'IF' statement above is responsible for which subroutine to run depending on what subroutine...
    #...is stored in the variable 'which_subroutine'


        if which_subroutine == 'mainGameSubroutine':
            if start_y > window_size[1]: #Once the y-position of the blue car exceeds the maximum height of the window
                start_y = -150 #Reset starting y-position
                random_lane = random.choice(lane) #Randomly choose next lane
                random_speed = random.choice(speed) #Randomly choose next speed
                count += 1 #Adds one to the number of cars dodged

            if start_y > player_coords[1] and random_lane == player_coords[0]: #Compares x and y positions of the cars
                which_subroutine = 'crash' #Sets variable to run the crash subroutine
            

        pygame.display.update() #Updates the disply with every repetition of the while loop
        clock.tick(60) #Sets frame rate to 60


game_loop() #Initially runs the main game loop
pygame.quit()
quit()

    
