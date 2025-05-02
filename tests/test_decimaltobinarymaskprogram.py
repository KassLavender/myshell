#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



class test_DecimalToBinaryMaskProgram(unittest.TestCase):
    def convert(self, data: str | int, answer: str):
        try:
            program = myprograms.DecimalToBinaryMaskProgram()
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(program.operation(data), answer)
    
    def unexpected(self, *args):
        print("There was a problem with testing the DecimalToBinaryMask program.")
        myutils.Error(*args)
        raise

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
        data = "123 I am a silly cat"
        answerStr = "Not an integer."
        
        try:
            with self.assertRaises(ValueError) as e:
                myprograms.DecimalToBinaryMaskProgram().operation(data)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)



if __name__ == '__main__':
    unittest.main()