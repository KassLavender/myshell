#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



data = 11111100
answer = -4



class test_binaryToIntegerProgram(unittest.TestCase):

    def test_convert_int(self):
        try:
            program = myprograms.binaryToIntegerProgram()
            self.assertEqual(program.operation(data), int(answer))
        except Exception as e:
            myutils.error(e)

if __name__ == '__main__':
    unittest.main()