#!/opt/homebrew/bin/python3.13 

import os
os.system('cls||clear')



class myProgram:
    def help (self) -> list[str]:
        for line in self.manual:
            print (line)



class binaryToNumberProgram(myProgram):

    def __init__(self):
        self.name = "binaryToNumber"

        self.prompt = "Enter binary number: "

        self.manual = ["In order to allow bit-wise operations, python represents negative numbers e.g. -4 as 111....11100.", " ","When given a string of binary values, outputs the decimal number that would be represented in Python."]

        self.operation = self.binaryToNumber

    def binaryToNumber(self, numberStr: str) -> str:

        sign = 1

        try:
            bitList = [int(x) for x in numberStr]
        except:
            raise ValueError("Not a number.")

        try:
            match int(bitList[0]):
                case 0: sign = 0
                case 1: sign = 1
                case _: raise ValueError(f"Not a binary number.")

            for i in range(len(bitList)):
                match int(bitList[i]):
                    case 0: bitList[i] = "1"
                    case 1: bitList[i] = "0"
                    case _: raise ValueError(f"Not binary number.")
        except Exception as e:
            raise e

        match (int(sign)):
            case 0: return (int("".join(bitList), 2) - 1)
            case 1: return -(int("".join(bitList), 2) + 1)







class numberToBinaryProgram(myProgram):

    def __init__(self):
        self.name = "numberToBinary"

        self.prompt = "Enter decimal number: "

        self.manual = ["In order to allow bit-wise operations, python represents negative numbers e.g. -4 as 111....11100.", " ","When given a decimal integer, outputs the binary number that would be represented in Python."]

        self.operation = self.numberToBinary
    
    def numberToBinary(self, number: int) -> int:
        return 4
    




