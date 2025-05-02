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
        answer = "11111100"
        self.convert(data, answer)
    
    def test_posInt(self):
        data = 11
        answer = "00001011"
        self.convert(data, answer)

    def test_negStr(self):
        data = "-7"
        answer = "11111001"
        self.convert(data, answer)
    
    def test_posStr(self):
        data = "12"
        answer = "00001100"
        self.convert(data, answer)

    def test_posIntLarge(self):
        data = 999999
        answer = "000011110100001000111111"
        self.convert(data, answer)

    def test_negIntLarge(self):
        data = -99999
        answer = "111111100111100101100001"
        self.convert(data, answer)

    def test_postIntMod8IsZero(self):
        data = 128
        answer = "0000000010000000"
        self.convert(data, answer)

    def test_negIntMod8IsZero(self):
        data = - 256
        answer = "1111111100000000"
        self.convert(data, answer)

    def test_zeroInt(self):
        data = 0
        answer = "00000000"
        self.convert(data, answer)

    def test_zeroStr(self):
        data = "0"
        answer = "00000000"
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