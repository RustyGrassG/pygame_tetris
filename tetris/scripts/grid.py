import pygame

class Grid():
    def __init__(self, game):
        self.game = game
        self.grid_size = (10, 20)
        self.grid = {}
        self.base_color = (10,10,10)
        self.objects = {}

        #sets up the grid and its associated values
        for y in range(self.grid_size[1]):
            for x in range(self.grid_size[0]):
                grid_key = str(x) + ',' + str(y)
                self.grid[grid_key] = {'pos': (x,y), 'active': 0, 'color': self.base_color}
    
    def clear_coord(self, location):
        pass

    def render(self):
        for key, value in self.objects.items():
                x_mod = 0
                y_mod = 0
                for i in range(len(value['size'])):
                    if value['size'][i] < 0:
                        x_mod = 0
                        y_mod += 1
                        continue
                    elif value['size'][i] > 0:
                        x_val = int(key[0]) + x_mod
                        y_val = int(key[-1]) + y_mod
                        coordinates = str(x_val) + ',' + str(y_val)
                        self.grid[coordinates]['color'] = (200,0,0)
                        self.grid[coordinates]['active'] = 1
                    x_mod += 1
                

        for key in self.grid:
            if self.grid[key]['active'] <= 0:
                color = self.base_color
            else:
                color = self.grid[key]['color']
            loc = self.grid[key]['pos']
            rect = pygame.Rect(loc[0], loc[1], 1, 1)

            pygame.draw.rect(self.game.tetris_display, color, rect)
    
    def spawn_object(self, location, object):
        self.objects[str(location[0]) + ',' + str(location[1])] = {'size': object, 'location': location}

    def clear_grid(self):
        self.objects.clear()
        for key, value in self.grid.items():
            #value['color'] = self.base_color
            value['active'] = 0
