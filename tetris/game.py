import pygame

import sys
import random

from scripts.utils import check_col
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

        #initalizing the clock
        self.clock = pygame.time.Clock()

        self.norm_speed = 1000
        self.fast_speed = 100
        self.current_speed = self.norm_speed

        self.MOVE_DOWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MOVE_DOWN_EVENT, self.current_speed)

        #self.assets = {}
        #self.blocks = []

        #Holds and sets the active object that is controlled by the player
        self.active_object = None
        self.get_piece([4,0], entities.pick_piece())
    
    #Made a def so it can be called more than once
    def get_piece(self, location, object):
        self.active_object = {'size': object['size'], 'shape': object['shape'], 'location': location, 'color': object['color']}
        print(self.active_object['size'])

    def check_below(self, object):
        for i in range(self.active_object['size'][0]):
            tile_to_check = (self.active_object['location'][0] + i, self.active_object['location'][1] + self.active_object['size'][1])
            if tile_to_check[1] < 20:
                tile_to_check = str(tile_to_check[0]) + ',' + str(tile_to_check[1])
                if self.grid.grid[tile_to_check]['active'] == 1:
                    return False
                else:
                    continue
            return True

    def run(self):
        while True:
            self.display.fill((0,0,0))
            self.grid.render()
            pressed_keys = pygame.key.get_pressed()


            #Checks if user is holding down the 's' key.
            #If true, the piece will move down at the faster rate (1 unit every 100ms)
            if pressed_keys[pygame.K_s] and self.current_speed != self.fast_speed:
                self.current_speed = self.fast_speed
                pygame.time.set_timer(self.MOVE_DOWN_EVENT, self.current_speed)
            if not pressed_keys[pygame.K_s] and self.current_speed != self.norm_speed:
                self.current_speed = self.norm_speed
                pygame.time.set_timer(self.MOVE_DOWN_EVENT, self.current_speed)
            
            

            for event in pygame.event.get():
                #Quits game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Moves piece down by 1 after a given amount of time
                if event.type == self.MOVE_DOWN_EVENT:
                    if self.active_object['location'][1] + self.active_object['size'][1] <= 19:
                            self.active_object['location'][1] += 1
                            if not self.check_below(self.active_object):
                                self.grid.set_piece(self.active_object)
                                self.get_piece([4,0], entities.pick_piece())
                    else:
                        self.grid.set_piece(self.active_object)
                        self.get_piece([4,0], entities.pick_piece())

                #Hadles movement
                if event.type == pygame.KEYDOWN:
                    #Clears the board(Debug)
                    if False:
                        if event.key == pygame.K_w:
                            print('clearing')
                            self.grid.clear_grid()
                    #Moves active piece left    
                    if event.key == pygame.K_a:
                        if self.active_object['location'][0] - 1 >= 0:
                            self.active_object['location'][0] -= 1
                    #Moves active piece right
                    if event.key == pygame.K_d:
                        if self.active_object['location'][0] + self.active_object['size'][0] <= 9:
                            self.active_object['location'][0] += 1
                    #Moves piece down at a faster rate
                    if event.key == pygame.K_s:
                        pygame.time.set_timer(self.MOVE_DOWN_EVENT, 100)
                    #prints the grid
                    if event.key == pygame.K_x:
                        #print(self.grid.grid)
                        check_col(self.active_object)
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_s:
                            pygame.time.set_timer(self.MOVE_DOWN_EVENT, 1000)
            

            #if pygame.time.get_ticks == 60:
                #self.active_object['location'][1] += 1
            #The outline of the game board
            board_outline_rect = pygame.Rect((self.screen.width // 2) - (self.tetris_res_upscale[0] // 2) - 4, (self.screen.height - self.tetris_res_upscale[1]) - 100, self.tetris_res_upscale[0] + 8, self.tetris_res_upscale[1] + 4)
            board_outline = pygame.draw.rect(self.display, (255,255,255), board_outline_rect)

            self.display.blit(pygame.transform.scale(self.tetris_display, self.tetris_res_upscale), ((self.screen.width // 2) - (self.tetris_res_upscale[0] // 2), (self.screen.height - self.tetris_res_upscale[1]) - 100))
            self.screen.blit(pygame.transform.scale(self.display, self.screen_res), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()