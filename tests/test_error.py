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

    def eval (self, answer: str, extractor: myutils.OutputExtractor):
        try:
            self.extractor = extractor
            self.outputStr = self.extractor.getOutput()
        except Exception as e:
            raise e
        finally:
            self.assertEqual(self.outputStr, answer)

    def unexpected(self, *args: Exception) -> print:
        print("There was a problem with creating a problem to be displayed by the error utility.")
        print(*args)

    def test_zeroExceptions(self):
        try:
            testError = self.createError()
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(self.answer0, extractor)
    
    def test_oneException(self):
        try:
            testError = self.createError(self.data1)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(self.answer1, extractor)

    def test_twoExceptions(self):
        try:
            testError = self.createError(self.data1, self.data2)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(self.answer2, extractor)

    def test_threeExceptions(self):
        try:
            testError = self.createError(self.data1, self.data2, self.data3)
            extractor = self.createExtractor(testError)
        except* Exception as e:
            self.unexpected(*e.exceptions)
            
        if 'extractor' in locals():
            self.eval(self.answer3, extractor)

    def test_error_notException(self):
        answerStr = "Cannot store Non-Exception object."
        error = []
        
        try:
            testError = self.createError(Exception(), "I am a silly cat")
        except* Exception as e:
            error = [*e.exceptions]
            
        if len(error) == 1:
            self.assertEqual(str(error[0]), answerStr)
        else:
            self.unexpected(*error)



if __name__ == '__main__':
    unittest.main()