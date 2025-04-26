#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



class test_binaryMaskToDecimalProgram(unittest.TestCase):

    def convert(self, data: str | int, answer: str | int):
        try:
            program = myprograms.binaryMaskToDecimalProgram()
        except Exception as e:
            myutils.error(e)
        
        self.assertEqual(program.operation(data), int(answer))

    def errorHandling(self, data: str | int):
        try:
            program = myprograms.binaryMaskToDecimalProgram()
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
        data = "abc"
        answerStr = "There was a problem executing the program: Not an integer.\n"
        errorStr = ""
        
        try:
            self.errorHandling(data)
        except Exception as e:
            try:
                errorStr = myutils.exceptionOutputExtraction(e)
            except Exception as e:
                #print("There was a problem while testing \"Not an integer\" error handling.")
                myutils.error(e)
        
        self.assertEqual(answerStr, errorStr)

    def test_error_notBinaryInt(self):
        data = "102"
        answerStr = "There was a problem executing the program: Not a binary integer.\n"
        errorStr = ""

        try:
            self.errorHandling(data)
        except Exception as e:
            try:
                errorStr = myutils.exceptionOutputExtraction(e)
            except Exception as f:
                print("There was a problem while testing \"Not a binary integer\" error handling.")
                myutils.error(f)
    
        self.assertEqual(answerStr, errorStr)


if __name__ == '__main__':
    unittest.main()