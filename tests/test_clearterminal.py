#!/usr/bin/env python3.13

import unittest
from unittest.mock import patch
import subprocess

from context import mycommands, myutils



class test_ClearTerminal(unittest.TestCase):
    def name_mock(name):
        def mocked(self):
            return name
        return mocked
    
    def unexpected(self, *args: Exception):
        print("There was a problem with testing the ClearTerminal command.")
        myutils.Error(*args)
        raise

    @patch("mycommands.ClearTerminal.getos_name",name_mock("nt"))
    def test_ClearTerminalNT(self):
            with patch("mycommands.ClearTerminal.run") as subprocess.run:
                try:
                    mycommands.ClearTerminal().operation()
                except* Exception as e:
                    self.unexpected(*e.exceptions)
                else:
                    subprocess.run.assert_called_once_with("cls", shell = True)

    @patch("mycommands.ClearTerminal.getos_name",name_mock("posix"))
    def test_clearTerminalOtherOS(self):
        with patch("mycommands.ClearTerminal.run") as subprocess.run:
            try:
                mycommands.ClearTerminal().operation()
            except* Exception as e:
                self.unexpected(*e.exceptions)
            else:
                subprocess.run.assert_called_once_with("clear")

        

if __name__ == '__main__':
    unittest.main()