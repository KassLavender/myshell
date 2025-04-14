#!/opt/homebrew/bin/python3.13

import os
os.system('cls||clear')



import unittest

from ..mycommands import mycommands

class test_binaryToIntegerProgram(unittest.TestCase):
    
    def test_convert_int(self):
        data = 110101
        result = binaryToIntegerProgram(data)
        self.assertEqual(result,-21)
    
if __name__ == '__main__':
    unittest.main()