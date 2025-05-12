import pygame
import random

from scripts.utils import get_size

pieces = {
            'o': [1,1,-1,
                  1,1],
            'i': [1,-1,
                  1,-1,
                  1,-1,
                  1,],
            's': [0,1,1,-1,
                  1,1],
            'z': [1,1,0,-1,
                  0,1,1],
            'l': [1,0,-1,
                  1,0,-1,
                  1,1],
            'j': [0,1,-1,
                  0,1,-1,
                  1,1],
            't': [1,1,1,-1,
                  0,1,0]
}

def pick_piece():
    options = ['o', 'i', 's', 'z', 'l', 'j', 't']
    colors = {
              'red': (255,0,0),
              'green': (0,255,0),
              'blue': (0,0,255),
              }
    piece = pieces[random.choice(options)]
    size = get_size(piece)

    
    piece = {'size': size, 'shape': piece, 'color': random.choice(list(colors.items()))}
    return piece