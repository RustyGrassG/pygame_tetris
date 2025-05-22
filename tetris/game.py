import pygame

import sys
import random

from scripts.utils import flat_to_matrix, matrix_to_flat, get_size, rotate_matrix_cw
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
        print(self.active_object['shape'])

    #Checks the collision to the left of the piece. Is only called when the player presses the 'a' key
    def check_left(self, object):
        size = object['size']
        location = object['location']
        #Goes through each piece in the active object
        for y in range(size[1]):
            for x in range(size[0]):
                #Sets the current coords of the active object segment
                coords = [location[0] + x, location[1] + y]
                if coords[0] - 1 < 0:
                    return False
                if self.grid.grid[f'{coords[0]},{coords[1]}']['active'] == 1:
                    if self.grid.grid[f'{coords[0] - 1},{coords[1]}']['active'] == 1 and not self.grid.grid[f'{coords[0] - 1},{coords[1]}']['in_use'] :
                        print('Blocked')
                        return False
        return True

    
    #Checks the collision to the right of the piece. Is only called when the player presses the 'd' key
    def check_right(self, object):
        size = object['size']
        location = object['location']
        #Goes through each piece in the active object
        for y in range(size[1]):
            for x in range(size[0]):
                #Sets the current coords of the active object segment
                coords = [location[0] + x, location[1] + y]
                if coords[0] + 1 > 9:
                    return False
                if self.grid.grid[f'{coords[0]},{coords[1]}']['active'] == 1:
                    if self.grid.grid[f'{coords[0] + 1},{coords[1]}']['active'] == 1 and not self.grid.grid[f'{coords[0] + 1},{coords[1]}']['in_use'] :
                        print('Blocked')
                        return False
        return True

    #Checks the location below the tile to see if it can be set or not
    def check_down(self, object) -> bool:
        size = object['size']
        #print(object['shape'])
        location = object['location']
        #Goes through each piece in the active object
        for y in range(size[1]):
            for x in range(size[0]):
                #Sets the current coords of the active object segment
                coords = [location[0] + x, location[1] + y]
                #print(coords)
                if coords[1] + 1 > 19:
                    return True
                if self.grid.grid[f'{coords[0]},{coords[1]}']['active'] == 1:
                    if self.grid.grid[f'{coords[0]},{coords[1] + 1}']['active'] == 1 and not self.grid.grid[f'{coords[0]},{coords[1] + 1}']['in_use'] :
                        print('Blocked')
                        return True
        
        return False
        

    #This is a definition that rotates a piece
    def rotate_piece(self, object):
        matrix = flat_to_matrix(object['shape'])
        rotated = rotate_matrix_cw(matrix)
        flat = matrix_to_flat(rotated)
        size = get_size(flat)
        print(f'{size}')
        if int(object['location'][0]) + size[0] > 9:
            print('goes')
            object['location'][0] += size[1] - size[0]
        object['shape'] = flat
        object['size'] = get_size(flat)

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
                    if self.check_down(self.active_object):
                        self.grid.set_piece(self.active_object)
                        self.get_piece([4,0], entities.pick_piece())
                    else:
                        self.active_object['location'][1] += 1
                    

                #Hadles movement
                if event.type == pygame.KEYDOWN:
                    #Clears the board(Debug)
                    if event.key == pygame.K_x:
                        print('clearing')
                        self.grid.clear_line(19)
                    #Moves active piece left    
                    if event.key == pygame.K_a:
                        if self.check_left(self.active_object):
                            self.active_object['location'][0] -= 1
                    #Moves active piece right
                    if event.key == pygame.K_d:
                        if self.check_right(self.active_object):
                            self.active_object['location'][0] += 1
                    #rotates piece
                    if event.key == pygame.K_w:
                        self.rotate_piece(self.active_object)
                    #Moves piece down at a faster rate
                    if event.key == pygame.K_s:
                        pygame.time.set_timer(self.MOVE_DOWN_EVENT, 100)
                    #Sets the time back to normal speeds for pieces
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_s:
                            pygame.time.set_timer(self.MOVE_DOWN_EVENT, self.norm_speed)
            

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