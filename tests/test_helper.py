#!/usr/bin/env python3.13

import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from context import myutils


class test_Helper(unittest.TestCase):

    def unexpected(self, *args):
        print("There was a problem with testing the Tokenizer util.")
        myutils.Error(*args)
        raise

    # When Helper prompts "With what command or program?:\n>>> ", gives input "cat".
    @patch('builtins.input', lambda *args: "cat")
    def test_oneWordHelp(self):
        answerStr = "cat"

        try:
            # Hides the new line printed after entering input.
            with redirect_stdout(StringIO()):
                outputStr = myutils.Helper(["help"])
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, answerStr)

    def test_twoWordHelp(self):
        answerStr = "cat"

        try:
            outputStr = myutils.Helper(["Help", "cat"])
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, answerStr)
    
    def test_threeOrMoreWordHelp(self):
        answerStr = "cat"

        try:
            outputStr = myutils.Helper(["Help", "cat", "how", "about", "that"])
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, answerStr)

    def test_error_notList(self):
        answerStr = "Helper can only accept a list of words as input."

        try:
            with self.assertRaises(AssertionError) as e:
                myutils.Helper(Exception("I am a cat"))
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_notListOfWords(self):
        answerStr = "Helper can only accept a list of words as input."

        try:
            with self.assertRaises(AssertionError) as e:
                myutils.Helper(["my", "cat", "is", 5])
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)


if __name__ == '__main__':
    unittest.main()