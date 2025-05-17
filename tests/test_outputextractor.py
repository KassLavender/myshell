#!/usr/bin/env python3.13

import unittest

from context import myutils



class test_OutputExtractor(unittest.TestCase):
    "Tests the OutputExtractor util."
    class SillyFunction():
        def operation(self):
            print("Meow!")
        
        def whoAmI(self):
            print("I am a silly cat.")

        def printColor(self, color: str):
            print(f"My color is {color}.")

        def countUp(self, num: int):
            print(num + 1)

    class OperationlessFunction():
        pass

    def unexpected(*args: Exception):
        print("There was a problem with testing the OutputExtractor util.")
        print(*args)
        raise
    
    def test_operation(self):
        answerStr = "Meow!\n"

        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(answerStr, extractor.getOutput())

    def test_otherMethod(self):
        answerStr = "I am a silly cat.\n"

        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            extractor.getOutput("whoAmI")
            self.assertEqual(answerStr, extractor.getOutput("whoAmI"))

    def test_otherMethodWithArgs(self):
        answerStr = "My color is orange.\n"

        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(answerStr, extractor.getOutput("printColor", "orange"))           

    def test_recursion(self):
        answerStr = "Meow!\n"
        
        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)

            for _ in range(100):
                extractor = myutils.OutputExtractor(extractor)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(answerStr, extractor.getOutput())

    def test_error_noOperation(self):
        answerStr = "Given object has no .operation() method."
        
        try:
            with self.assertRaises(AssertionError) as e:
                myutils.OutputExtractor(self.OperationlessFunction)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_doesNotHaveFunction(self):
        answerStr = "\"SillyFunction\" has no method \"notafunction\"."
        try:
            with self.assertRaises(Exception) as e:
                silly = self.SillyFunction()
                extractor = myutils.OutputExtractor(silly)
                extractor.getOutput("notafunction")
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_functionIssueWithArguments(self):
        answerStr = "An unexpected error occurred with the OutputExtractor output function: test_OutputExtractor.SillyFunction.whoAmI() takes 1 positional argument but 3 were given"

        try:
            with self.assertRaises(Exception) as e:
                silly = self.SillyFunction()
                extractor = myutils.OutputExtractor(silly)
                extractor.getOutput("whoAmI", "kitty", "cat")
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_functionIssueInternal(self):
        answerStr = "An unexpected error occurred with the OutputExtractor output function: unsupported operand type(s) for +: 'Exception' and 'int'"

        try:
            with self.assertRaises(Exception) as e:
                silly = self.SillyFunction()
                extractor = myutils.OutputExtractor(silly)
                extractor.getOutput("countUp", Exception(4))
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

if __name__ == '__main__':
    unittest.main()