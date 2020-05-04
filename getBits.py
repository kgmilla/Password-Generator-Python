""" for emulating the gpio input of a breakdown 
    p-n junction random bit generator"""

import random

def generateRandBit():
    return random.randint(0,1)