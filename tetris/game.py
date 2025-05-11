import pygame

import sys
import random

from scripts.grid import Grid
import scripts.entities as entities

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()


        pygame.display.set_caption('Tetris')

        #display window
        self.screen_res = (720, 1280)
        #tetris game board resolution. This is the actual tetris pieces
        self.tetris_res = (10, 20)
        self.tetris_res_upscale = (420,840)

        #Window
        self.screen = pygame.display.set_mode(self.screen_res)
        #Display overlay
        self.display = pygame.Surface(self.screen_res)
        #Tetris Board
        self.tetris_display = pygame.Surface(self.tetris_res)
        self.grid = Grid(self)

        self.clock = pygame.time.Clock()

        self.assets = {}

        self.blocks = []

        self.movement = [False, False, False, False]


        
        self.grid.spawn_object((4,0), entities.pieces[entities.pick_piece()])
    

    def run(self):
        while True:
            self.display.fill((0,0,0))
            self.grid.render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        print('clearing')
                        self.grid.clear_grid()
            

            #The outline of the game board
            board_outline_rect = pygame.Rect((self.screen.width // 2) - (self.tetris_res_upscale[0] // 2) - 4, (self.screen.height - self.tetris_res_upscale[1]) - 100, self.tetris_res_upscale[0] + 8, self.tetris_res_upscale[1] + 4)
            board_outline = pygame.draw.rect(self.display, (255,255,255), board_outline_rect)

            self.display.blit(pygame.transform.scale(self.tetris_display, self.tetris_res_upscale), ((self.screen.width // 2) - (self.tetris_res_upscale[0] // 2), (self.screen.height - self.tetris_res_upscale[1]) - 100))
            self.screen.blit(pygame.transform.scale(self.display, self.screen_res), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()