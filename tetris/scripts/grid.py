import pygame

class Grid():
    def __init__(self, game):
        self.game = game
        self.grid_size = (10, 20)
        self.grid = {}
        self.base_color = (10,10,10)
        #Holds all the active grid points, so that they wont disappear 
        self.active_spaces = []

        #sets up the grid and its associated values
        for y in range(self.grid_size[1]):
            for x in range(self.grid_size[0]):
                grid_key = str(x) + ',' + str(y)
                self.grid[grid_key] = {'pos': (x,y), 'active': 0, 'color': self.base_color, 'in_use': False}

    def render(self):
        self.update()
        if self.game.active_object:
            cur_object = self.game.active_object
            x_mod = 0
            y_mod = 0
            for i in range(len(cur_object['shape'])):
                if cur_object['shape'][i] < 0:
                    x_mod = 0
                    y_mod += 1
                    continue
                elif cur_object['shape'][i] > 0:
                    x_val = int(cur_object['location'][0]) + x_mod
                    y_val = int(cur_object['location'][1]) + y_mod
                    coordinates = str(x_val) + ',' + str(y_val)
                    self.grid[coordinates]['color'] = cur_object['color'][1]
                    self.grid[coordinates]['active'] = 1
                    self.grid[coordinates]['in_use'] = True
                    #This is the problem
                x_mod += 1
                

        for key in self.grid:
            if self.grid[key]['active'] <= 0:
                color = self.base_color
            else:
                if self.grid[key] in self.active_spaces:
                    color = (255,0,255)
                color = self.grid[key]['color']
            loc = self.grid[key]['pos']
            rect = pygame.Rect(loc[0], loc[1], 1, 1)

            pygame.draw.rect(self.game.tetris_display, color, rect)

    def update(self):
        for key, value in self.grid.items():
            if key in self.active_spaces:
                value['active'] = 1
            else:
                value['active'] = 0
            
    
    def set_piece(self, object):
        object = self.game.active_object
        x_mod = 0
        y_mod = 0
        for i in range(len(object['shape'])):
            if object['shape'][i] < 0:
                x_mod = 0
                y_mod += 1
                continue
            elif object['shape'][i] > 0:
                x_val = int(object['location'][0]) + x_mod
                y_val = int(object['location'][1]) + y_mod
                coordinates = str(x_val) + ',' + str(y_val)
                self.grid[coordinates]['color'] = object['color'][1]
                self.grid[coordinates]['active'] = 1
                self.grid[coordinates]['in_use'] = False
                self.active_spaces.append(str(x_val) + ',' + str(y_val))
            x_mod += 1
        self.check_completed()
    
    #This checks the completed lines on the tetris board, stores them, then called the 'clear line'
    #Function for each cleared line
    #THIS SHOULD ONLY BE CALLED AFTER A PIECE IS SET
    def check_completed(self):
        #Only needs the y-value inserted into the list
        completed_lines = []
        #Next i need to iterate through each row and see if the line is cleared
        for y in range(self.grid_size[1]):
            is_completed = True
            for x in range(self.grid_size[0]):
                coords = str(x) + ',' + str(y)
                if self.grid[coords]['active'] == 0:
                    is_completed = False
            if is_completed:
                self.clear_line(y)
                completed_lines.append(y)
        if len(completed_lines) > 0:
            self.lower_top(completed_lines)
            self.game.add_score(len(completed_lines))

    def lower_top(self, lines:list):
        lines = sorted(lines)

        num_cleared_below = 0

        for target_y in range(self.grid_size[1] - 1, -1, -1):
            if target_y in lines:
                num_cleared_below += 1
                continue

            new_y = target_y + num_cleared_below

            for x in range(self.grid_size[0]):
                from_coords = f"{x},{target_y}"
                to_coords = f"{x},{new_y}"

                self.grid[to_coords]['active'] = self.grid[from_coords]['active']
                self.grid[to_coords]['color'] = self.grid[from_coords]['color']
                self.grid[to_coords]['in_use'] = self.grid[from_coords]['in_use']

                if from_coords in self.active_spaces:
                    self.active_spaces.append(to_coords)
                    self.active_spaces.remove(from_coords)
                    
            for y in range(num_cleared_below):
                for x in range(self.grid_size[0]):
                    top_coords = f'{x},{y}'
                    self.grid[top_coords]['active'] = 0
                    self.grid[top_coords]['color'] = self.base_color
                    self.grid[top_coords]['in_use'] = False
                    if top_coords in self.active_spaces:
                        self.active_spaces.remove(top_coords)


    #Clears any location in the grid and removes it from the active spaces
    def clear_pixel(self, coordinate:str):
        location = self.grid[coordinate]
        location['active'] = 0
        location['in_use'] = False
        for x in range(0, len(self.active_spaces)):
            if coordinate == self.active_spaces[x]:
                self.active_spaces.pop(x)
                return

    #This clears the entire xlevel at any given y level
    def clear_line(self, y_level:int):
        for x in range(self.grid_size[0]):
            coords = str(x) + ',' + str(y_level)
            self.clear_pixel(coords)
        

    def clear_grid(self):
        for key, value in self.grid.items():
            value['active'] = 0
            value['in_use'] = False
            self.active_spaces.clear()
