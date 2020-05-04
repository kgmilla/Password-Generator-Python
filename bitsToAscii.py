#Creates an array of 7 bits, thus turning
#8 bits into a bitArr
import getBits
import numpy

decimalConversion = [64, 32, 16, 8, 4, 2, 1]

def bit2BitArr():
    """This function uses an input source
    that produces a random bit(1 or 0) and 
    places it into an array of 7 bits"""
    bitArr = numpy.empty(7, dtype=int)
    for x in range(7):
        randBit = getBits.generateRandBit()
        bitArr[x] = randBit
    return bitArr
    

def bitArrToDecimal(bitArr):
    """This function takes value bitArr
    an array of 7 bits and returns it in
    decimal form"""
    decimalForm = 0
    for x in range(7):
        if(bitArr[x] == 1):
            decimalForm += decimalConversion[x]
        else:
            continue
    return decimalForm



def decimalToAscii(decimalForm):
    """This function takes in a Decimal number
    from decimalForm and only converts values for
    numbers, letters, and special characters"""
    if(decimalForm > 32 and decimalForm < 128):
        asciiChar = chr(decimalForm)
        return asciiChar


def createAsciiStr(length):
    """This function takes the desired 
    password length and uses characters
    gerated from random bits to ascii and creates
    a string of those characters"""
    password = ""
    while(len(password) < length):
        character = decimalToAscii(bitArrToDecimal(bit2BitArr()))
        if(character != None):
            password = password + character
    return password
    

