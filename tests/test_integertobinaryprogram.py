#!/opt/homebrew/bin/python3.13

import unittest

from context import myprograms, myutils



data = -4
answer = 1100



class test_integerToBinaryProgram(unittest.TestCase):
    
    def test_convert_binary_int(self):
        try:
            program = myprograms.integerToBinaryProgram()
            program.operation(data)
            self.assertEqual(program.operation(data), int(answer))
        except Exception as e:
            myutils.error(e)

if __name__ == '__main__':
    unittest.main()