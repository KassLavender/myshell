#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



class test_BinaryMaskToDecimalProgram(unittest.TestCase):
    def convert(self, data: str | int, answer: int):
        try:
            program = myprograms.BinaryMaskToDecimalProgram()
        except* Exception as e:
            print("There was a problem with testing the BinaryMaskToDecimal program.")
            myutils.Error(*e.exceptions)
            
        if 'program' in locals():
            self.assertEqual(program.operation(data), answer)

    def errorHandling(self, data: str | int):
        try:
            program = myprograms.BinaryMaskToDecimalProgram()
            program.operation(data)
        except Exception as e:
            raise e

    def test_negInt(self):
        data = 1111100
        answer = -4
        self.convert(data, answer)
    
    def test_negStr(self):
        data = "11101"
        answer = -3
        self.convert(data, answer)

    def test_posStr(self):
        data = "000011"
        answer = 3
        self.convert(data, answer)
    
    def test_zeroInt(self):
        data = 0000
        answer = 0
        self.convert(data, answer)

    def test_zeroStr(self):
        data = "0"
        answer = 0
        self.convert(data, answer)

    def test_error_notInt(self):
        data = "I am a silly cat"
        answerStr = "Not an integer."
        error = []
        
        try:
            self.errorHandling(data)
        except* Exception as e:
            error = [*e.exceptions]
        
        if len(error) == 1:
            self.assertEqual(str(error[0]), answerStr)
        else:
            print("There was a problem while testing \"Not an integer\" error handling.")
            myutils.Error(*error)

    def test_error_notBinaryInt(self):
        data = "102"
        answerStr = "Not a binary integer."
        error = []

        try:
            self.errorHandling(data)
        except* Exception as e:
                error = [*e.exceptions]

        if len(error) == 1:
            self.assertEqual(str(error[0]), answerStr)
        else:
            print("There was a problem while testing \"Not a binary integer\" error handling.")
            myutils.Error(*error)



if __name__ == '__main__':
    unittest.main()