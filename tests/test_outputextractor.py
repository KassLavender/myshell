#!/opt/homebrew/bin/python3.13

import unittest

from context import myutils


class test_OutputExtractor(unittest.TestCase):
    "Tests the OutputExtractor util."
    class SillyFunction():
        def operation(self):
            print("Meow!")

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

    def test_recursion(self):
        answerStr = "Meow!\n"
        
        try:
            silly = self.SillyFunction()
            extractor = myutils.OutputExtractor(silly)

            for i in range(100):
                extractor = myutils.OutputExtractor(extractor)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(answerStr, extractor.getOutput())

    def test_error_noOperation(self):
        answerStr = "Given object has no .operation() method."

        with self.assertRaises(AttributeError) as e:
            myutils.OutputExtractor(self.OperationlessFunction)

        outputStr = str(e.exception)
        self.assertEqual(outputStr, answerStr)



if __name__ == '__main__':
    unittest.main()