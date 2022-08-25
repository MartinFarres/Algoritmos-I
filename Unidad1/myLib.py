from algo1 import *


# Validaciones

def valInt(placeHolder, sit=None):
    while True:
        num = input_int(placeHolder)
        if sit != None:
            if type(num) == int and num > sit:
                return num
