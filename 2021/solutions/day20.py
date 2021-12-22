# Using convolutions in numpy

import numpy as np
from scipy.ndimage import convolve
from itertools import combinations

def read_file(test = True):
    if test:
        filename = '../tests/day20.txt'
    else:
        filename = '../input/day20.txt'
    with open(filename) as file:
        image = list()
        for i, line in enumerate(file):
            if i == 0:
                algorithm = np.array([int(char == "#") for char in line.strip()]) 
            elif line.strip():
                image.append(line.strip())
    image = np.pad([[int(char == "#") for char in row] for row in image], (51,51))
    return algorithm, image
            
        
    
def print_set(input_set):
    pass

def puzzle1(test = True):
    alg, img = read_file(test)
    
    # kernel for convolution
    kernel = 2**np.arange(9).reshape(3,3)
    
    for i in range(2):
        
        # compute number for each pixel
        temp = convolve(img, kernel)
        
        # apply algorithm to light/dim each pixel
        img = alg[temp]
    print(img.sum())
                    

def puzzle2(test = True):
    alg, img = read_file(test)
    
    # kernel for convolution
    kernel = 2**np.arange(9).reshape(3,3)
    
    for i in range(50):
        # compute number for each pixel
        temp = convolve(img, kernel)
        
        # apply algorithm to light/dim each pixel
        img = alg[temp]
    print(img.sum())


puzzle1()
puzzle2()
