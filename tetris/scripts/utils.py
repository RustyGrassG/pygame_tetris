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