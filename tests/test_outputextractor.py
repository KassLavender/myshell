#!/opt/homebrew/bin/python3.13

import unittest

from context import myutils


class test_OutputExtractor(unittest.TestCase):
    class SillyFunction():
        def operation(self):
            print("Meow!")

    class OperationlessFunction():
        pass

    def unexpected(*args: Exception):
        print("There was a problem with testing the OutputExtractor util.")
        print(*args)
    
    def test_operation(self):
        answerStr = "Meow!\n"

        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        
        if 'extractor' in locals():
            self.assertEqual(answerStr, extractor.getOutput())

    def test_recursion(self):
        answerStr = "Meow!\n"
        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)

            for i in range(100):
                extractor = myutils.OutputExtractor(extractor)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.assertEqual(answerStr, extractor.getOutput())

    def test_error_noOperation(self):
        answerStr = "Given object has no .operation() method."
        error = []

        try:
            extractor = myutils.OutputExtractor(self.OperationlessFunction)
        except* Exception as e:
            error = [*e.exceptions]
        
        if len(error) == 1:
            self.assertEqual(str(error[0]), answerStr)
        else:
            self.unexpected(*error)



if __name__ == '__main__':
    unittest.main()