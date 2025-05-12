import pygame

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
        print(strin)


def get_size(object):
    size_x = 0
    size_y = 1
    x = 0
    for i in object:
      if i != -1:
            x += 1
      else:
            if x > size_x:
                  size_x = x
            x = 0
            size_y += 1
    
    return size_x, size_y