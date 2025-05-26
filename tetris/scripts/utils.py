import pygame

def level_to_drop_speed(level):
    level_dic = {
        1: [1000, 100],
        2: [950, 95],
        3: [900, 90],
        4: [850, 85],
        5: [800, 80],
        6: [750, 75],
        7: [700, 70],
        8: [650, 65],
        9: [600, 60],
        10: [550, 55],
        11: [500, 50],
        12: [475, 47],
        13: [450, 45],
        14: [425, 42],
        15: [400, 40],
        16: [375, 37],
        17: [350, 35],
        18: [325, 32],
        19: [300, 30],
        20: [275, 30],
    }
    if level < 20:
        return level_dic[level]
    else:
        return level_dic[20]

#Checks and returns any colision on the piece
#Any colision downwards on check will set the piece in place
def check_col(object):
    padding = 2
    #tuple
    size = object['size']
    #Adds padding to both sizes
    size_x = size[0] + padding
    size_y = size[1] + padding
    for len in range(size_y):
        strin = ''
        for len_x in range(size_x):
            strin += '0'


def get_size(object):
    matrix = flat_to_matrix(object)
    size_x = len(matrix[0])
    size_y = len(matrix)
    
    return size_x, size_y

def flat_to_matrix(flat_shape):
    matrix = []
    row = []
    for val in flat_shape:
        if val == -1:
            matrix.append(row)
            row = []
        else:
            row.append(val)
    if row:
        matrix.append(row)
    return matrix

def matrix_to_flat(matrix):
    flat = []
    for row in matrix:
        flat.extend(row)
        flat.append(-1)
    flat.pop()  # Remove last -1
    return flat

def rotate_matrix_cw(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

class Display_Text:
    def __init__(self, text: str, game, render_location: list, size: int, font: str, color = (255,255,255)):
        pygame.font.init()

        self.size = size
        self.font = pygame.font.SysFont(font, self.size)
        self.location = render_location
        self.game = game
        self.text = text
        self.color = color
        

    def update(self, text = None, render_location = None, size = None, font = None, color = None):
        if size:
            self.size = size
        if font:
            self.font = pygame.font.SysFont(font, self.size)
        if render_location:
            self.location = render_location
        if text:
            self.text = text
        if color:
            self.color = color
    
    def render_text(self, surface):
        text_surface = self.font.render(self.text, False, self.color)
        surface.blit(text_surface, (self.location[0], self.location[1]))
        