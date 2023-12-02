'''Functions to calculate right triangle measurements'''

from math import sqrt

def calcArea(adjacent, opposite):
    '''Calculates the area of a right triangle'''
    return (adjacent * opposite) / 2

def calcHypotenuse(adjacent, opposite):
    '''Calculates the hypotenuse of a right triangle'''
    return sqrt((adjacent**2) + (opposite**2))