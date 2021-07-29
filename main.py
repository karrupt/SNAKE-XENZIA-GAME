import math
import time

import pygame
import random
from pygame import mixer
pygame.init()
game_width = 800
game_height = 760
game_screen = pygame.display.set_mode((game_width, game_height)) # creating a gamescreen of 800 * 800 pixels
game_state = "running"
pygame.display.set_caption("The Snake Game")
icon = pygame.image.load("png/snake game icon.png")
pygame.display.set_icon(icon)
head_width = 40
head_height = 40
head = pygame.image.load("png/sanke_head.png")
tail = pygame.image.load("png/sanke_body.png")
def rdm_coordinates():
    x = math.floor( (random.randint(1, 760)) / head_width)
    y = math.floor( (random.randint(1, 760)) / head_height)
    return  x *head_width , y*head_height

def calc_dis(x1, y1, x2, y2):
    return math.sqrt(pow(x1- x2, 2) + math.pow(y1 - y2, 2))

head_x, head_y = 760 , 0
head_xchange = 0
head_ychange = 0
snake = [ [head_x, head_y]]
snake_direction = ""
mixer.music.load("music/Snake Game - Theme Song.mp3")
mixer.music.play(-1)
eating_sound = mixer.Sound("music/Eating ! Sound.mp3")
# print(snake)
dummy_snake = []
snake_length = 1
start_game = False
game_over = False
game_over_font = pygame.font.Font("freesansbold.ttf", 70)
game_over_text = game_over_font.render("!! GAME OVER !!", True, (0, 0, 0))
food = pygame.image.load("png/food.png")
foodx , foody = rdm_coordinates()
food_eaten = False
player_score = 0
score_font = pygame.font.SysFont("arial", 40)
score = "Score: " + str(player_score)
score_text = score_font.render(score, True, (9, 101, 222))
game_over_music = mixer.Sound("music/Game Over.mp3")
while game_state == "running":
    game_screen.fill((240 ,240 , 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "stop"
        if event.type == pygame.KEYDOWN:
            start_game = True
            if event.key == pygame.K_LEFT:
                if snake_direction != "right":
                    head_xchange = -40
                    head_ychange = 0
                    snake_direction = "left"
            elif event.key == pygame.K_RIGHT:
                if snake_direction != "left":
                    head_xchange = 40
                    head_ychange = 0
                    snake_direction = "right"
            elif event.key == pygame.K_DOWN:
                if snake_direction != "up":
                    head_ychange = 40
                    head_xchange = 0
                    snake_direction = "down"
            elif event.key == pygame.K_UP:
                if snake_direction != "down":
                    head_ychange = -40
                    head_xchange = 0
                    snake_direction = "up"
    if game_over == False:
        head_x += head_xchange
        if head_x < 0:
            # game_over = True # by making this line uncommented, the left boundary will act as a game over wall
            head_x = 760
        elif head_x >= 800:
            # game_over = True # by making this line uncommented, the right boundary will act as a game over wall
            head_x = 0
        head_y += head_ychange
        if head_y < 0:
            # game_over = True # by making this line uncommented, the top boundary will act as a game over wall
            head_y = 720
        elif head_y >= 760:
            # game_over = True # by making this line uncommented, the bottom boundary will act as a game over wall
            head_y = 0
        temp = [[head_x, head_y]]
        temp_head = [head_x, head_y]
        if temp_head in snake[:-1]:
            game_over = True
            game_over_music.play()
        for i in range(snake_length - 1):
            temp.append([snake[i][0], snake[i][1]])

        snake = temp

        for i in range(snake_length ):
            if i:
                game_screen.blit(tail, (snake[i][0],snake[i][1]))
            else:
                game_screen.blit(head, (head_x, head_y))
        if calc_dis(head_x, head_y, foodx, foody) < 1:
            eating_sound.play()
            food_eaten = True
            snake.append([foodx, foody])
            snake_length += 1
            player_score += 1
        if food_eaten == True:
            foodx, foody = rdm_coordinates()
            food_eaten = False
        game_screen.blit(food, (foodx, foody))
        score = "Score: " + str(player_score)
        score_text = score_font.render(score, True, (9, 101, 222))
        game_screen.blit(score_text, (10, 10))
    else:
        mixer.music.stop()
        score_font = pygame.font.SysFont("georgia", 60)
        score = "Score: " + str(player_score)
        score_text = score_font.render(score, True, (9, 101, 222))
        game_screen.blit(score_text, (250, 200))
        game_screen.blit(game_over_text, (150, 350))
    pygame.display.update()
    pygame.time.Clock().tick(6) # setting the frame per second of the clock to be 6
