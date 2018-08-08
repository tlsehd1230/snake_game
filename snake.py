import pygame
import random
from color import *

pygame.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("snake game")

clock = pygame.time.Clock()

block_size = 20

FPS = 20

font_50 = pygame.font.SysFont("D2Coding", 50)
font_20 = pygame.font.SysFont("D2Coding", 20)

def main() :
    started = False
    gameTerminate = False
    gameover = False
    lead_X = display_width / 2
    lead_Y = display_height / 2
    speed_X = 0
    speed_Y = 0
    snakeLength = 1
    snake_list = [(lead_X, lead_Y)]
    random_X = random.randrange(0, (display_width / block_size) // 1) * block_size
    random_Y = random.randrange(0, (display_height / block_size) // 1) * block_size
    total_score = 0

    while not gameTerminate :
        if gameover :
            game_display.fill(red)
            label = font_50.render("GameOver", True, white)
            label2 = font_20.render("press C to continue", True, white)
            label3 = font_20.render("press Q to quit", True, white)

            width = label.get_width()
            game_display.blit(label, ((display_width - width) / 2, 200))

            width = label2.get_width()
            game_display.blit(label2, ((display_width - width) / 2, 300))

            width = label3.get_width()
            game_display.blit(label3, ((display_width - width) / 2, 350))

            pygame.display.update()

            for event in pygame.event.get() :
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or event.type == pygame.QUIT :
                    gameTerminate = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_c :
                    gameover = False
                    lead_X = display_width / 2
                    lead_Y = display_height / 2
                    speed_X = 0
                    speed_Y = 0
                    snake_list = [(lead_X, lead_Y)]
                    started = False
                    random_X = random.randrange(0, (display_width / block_size) // 1) * block_size
                    random_Y = random.randrange(0, (display_height / block_size) // 1) * block_size
                    snakeLength = 1

        if not gameover :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    gameTerminate = True

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP and speed_Y == 0 :
                        started = True
                        speed_X = 0
                        speed_Y = -block_size

                    if event.key == pygame.K_DOWN and speed_Y == 0 :
                        started = True
                        speed_X = 0
                        speed_Y = block_size

                    if event.key == pygame.K_LEFT and speed_X == 0 :
                        started = True
                        speed_X = -block_size
                        speed_Y = 0

                    if event.key == pygame.K_RIGHT and speed_X == 0 :
                        started = True
                        speed_X = block_size
                        speed_Y = 0


            lead_X += speed_X
            lead_Y += speed_Y

            if (lead_X  < 0 or lead_X >= display_width) or (lead_Y < 0 or lead_Y >= display_height) :
                gameover = True

            if started :
                snake_list.append((lead_X,lead_Y))
            if len(snake_list) > snakeLength :
                del snake_list[0]

            if snake_list[-1] in snake_list[:-1] :
                gameover = True

            if (random_X, random_Y) == snake_list[-1] :
                snakeLength += 1
                random_X = random.randrange(0, (display_width / block_size) // 1) * block_size
                random_Y = random.randrange(0, (display_height / block_size) // 1) * block_size

            game_display.fill(black)

            total_score = font_50.render(str(snakeLength - 1), True, white)
            score_width = total_score.get_width()
            score_height = total_score.get_height()
            game_display.blit(total_score, ((display_width - score_width) / 2, 30))

            pygame.draw.rect(game_display, red, (random_X, random_Y, block_size, block_size))

            for k in snake_list :
                pygame.draw.rect(game_display, green, (k[0], k[1], block_size, block_size))

            clock.tick(FPS)
            pygame.display.update()



main()
