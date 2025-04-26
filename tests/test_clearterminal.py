#!/opt/homebrew/bin/python3.13

import unittest
from unittest.mock import patch
from subprocess import run

from context import mycommands, myutils



class test_ClearTerminal(unittest.TestCase):
    def test_ClearTerminal(self):
        try:
            with patch("mycommands.ClearTerminal.run") as run:
                mycommands.ClearTerminal().operation()
                run.assert_called_once_with('clear||cls', shell=True)
        except* Exception as e:
            myutils.Error(*e.exceptions)

        

if __name__ == '__main__':
    unittest.main()