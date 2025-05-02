#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



class test_BinaryMaskToDecimalProgram(unittest.TestCase):
    def convert(self, data: str | int, answer: int):
        try:
            program = myprograms.BinaryMaskToDecimalProgram()
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(program.operation(data), answer)

    def unexpected(self, *args):
        print("There was a problem with testing the BinaryMaskToDecimal program.")
        myutils.Error(*args)
        raise

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

        with self.assertRaises(ValueError) as e:
            myprograms.BinaryMaskToDecimalProgram().operation(data)
        
        outputStr = str(e.exception)
        self.assertEqual(outputStr, answerStr)

    def test_error_notBinaryInt(self):
        data = "102"
        answerStr = "Not a binary integer."

        with self.assertRaises(ValueError) as e:
            myprograms.BinaryMaskToDecimalProgram().operation(data)
        
        outputStr = str(e.exception)
        self.assertEqual(outputStr, answerStr)



if __name__ == '__main__':
    unittest.main()