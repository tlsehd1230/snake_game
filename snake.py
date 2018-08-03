import pygame
import random
from color import *

pygame.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("snake game")

clock = pygame.time.Clock()

block_size = 10

FPS = 30

font_50 = pygame.font.SysFont("D2Coding", 50)
font_20 = pygame.font.SysFont("D2Coding", 20)

def main() :

    gameTerminate = False
    gameover = False

    while not gameTerminate :
        if gameover :
            game_display.fill(black)
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

            

main()
