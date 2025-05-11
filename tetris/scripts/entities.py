import pygame
import random

pieces = {
            'o': [1,1,-1,
                  1,1],
            'i': [1,-1,
                  1,-1,
                  1,-1,
                  1,-1,],
            's': [0,1,1,-1,
                  1,1],
            'z': [1,1,-1,
                  0,1,1],
            'l': [1,-1,
                  1,-1,
                  1,1],
            'j': [0,1,-1,
                  0,1,-1,
                  1,1],
            't': [1,1,1,-1,
                  0,1]
}

def pick_piece():
    options = ['o', 'i', 's', 'z', 'l', 'j', 't']
    piece = random.choice(options)
    return piece