#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



class test_decimalToBinaryMaskProgram(unittest.TestCase):
    
    def convert(self, data: str | int, answer: str | int):
        try:
            program = myprograms.decimalToBinaryMaskProgram()
        except Exception as e:
            myutils.error(e)

            self.assertEqual(program.operation(data), answer)
    
    def errorHandling(self, data: str | int):
        try:
            program = myprograms.decimalToBinaryMaskProgram()
            program.operation(data)
        except Exception as e:
            raise e

    def test_negInt(self):
        data = -4
        answer = "100"
        self.convert(data, answer)
    
    def test_posInt(self):
        data = 11
        answer = "01011"
        self.convert(data, answer)

    def test_negStr(self):
        data = "-7"
        answer = "1001"
        self.convert(data, answer)
    
    def test_posStr(self):
        data = "12"
        answer = "01100"
        self.convert(data, answer)
    
    def test_zeroInt(self):
        data = 0
        answer = "0"
        self.convert(data, answer)

    def test_zeroStr(self):
        data = "0"
        answer = "0"
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


if __name__ == '__main__':
    unittest.main()