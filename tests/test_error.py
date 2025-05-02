#!/opt/homebrew/bin/python3.13

import unittest
from io import StringIO
from contextlib import redirect_stdout

from context import myutils



class test_Error(unittest.TestCase):
    data1 = Exception("First error.")
    data2 = Exception("Second error.")
    data3 = Exception("Third error.")
    answer0 = ""
    answer1 = "There was a problem executing the program: First error.\n"
    answer2 = answer1 + "There was a problem executing the program: Second error.\n"
    answer3 = answer2 + "There was a problem executing the program: Third error.\n"

    def createError(self, *args: Exception) -> myutils.Error:
        try:
            with redirect_stdout(StringIO()):
                error = myutils.Error(*args)
            return error
        except Exception as e:
            raise e
    
    def createExtractor(self, error: myutils.Error) -> myutils.OutputExtractor:
        try:
            extractor = myutils.OutputExtractor(error)
            return extractor
        except Exception as e:
            raise e

    def eval(self, extractor: myutils.OutputExtractor, answer: str):
        try:
            self.extractor = extractor
            self.outputStr = self.extractor.getOutput()
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(self.outputStr, answer)

    def unexpected(self, *args: Exception) -> print:
        print("There was a problem with creating a problem to be displayed by the error utility.")
        for arg in args:
            print(arg)
        raise

    def test_zeroExceptions(self):
        try:
            testError = self.createError()
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.eval(extractor, self.answer0)
    
    def test_oneException(self):
        try:
            testError = self.createError(self.data1)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.eval(extractor, self.answer1)

    def test_twoExceptions(self):
        try:
            testError = self.createError(self.data1, self.data2)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.eval(extractor, self.answer2)

    def test_threeExceptions(self):
        try:
            testError = self.createError(self.data1, self.data2, self.data3)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.eval(extractor, self.answer3)

    def test_error_notException(self):
        answerStr = "Cannot store Non-Exception object."

        with self.assertRaises(ValueError) as e:
            self.createError("I am a silly cat")
        
        outputStr = str(e.exception)
        self.assertEqual(outputStr, answerStr)



if __name__ == '__main__':
    unittest.main()