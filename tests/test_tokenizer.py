#!/usr/bin/env python3.13

import unittest

from context import myutils



class test_Tokenizer(unittest.TestCase):
    def unexpected(self, *args):
        print("There was a problem with testing the Tokenizer util.")
        myutils.Error(*args)
        raise
    
    def test_emptyString(self):
        answerList = []

        try:
            outputList = myutils.Tokenizer("")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList,answerList)

    def test_emptyStringWithSpaces(self):
        answerList = []

        try:
            outputList = myutils.Tokenizer("    ")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList,answerList)           
    
    def test_oneWordString(self):
        answerList = ["cat"]

        try:
            outputList = myutils.Tokenizer("cat")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_oneWordStringWithSpaces(self):
        answerList = ["cat"]

        try:
            outputList = myutils.Tokenizer("    cat        ")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_twoWordString(self):
        answerList = ["silly","cat"]

        try:
            outputList = myutils.Tokenizer("silly cat")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_twoWordStringWithManySpaces(self):
        answerList = ["silly","cat"]

        try:
            outputList = myutils.Tokenizer(" silly      cat   ")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_threeWordString(self):
        answerList = ["my","silly","cat"]

        try:
            outputList = myutils.Tokenizer("my silly cat")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_threeWordStringWithManySpaces(self):
        answerList = ["my","silly","cat"]

        try:
            outputList = myutils.Tokenizer("  my    silly  cat    ")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputList, answerList)

    def test_Error_TypeError(self):
        answerStr = "Tokenizer can only accept a string as input."

        try:
            with self.assertRaises(AssertionError) as e:
                myutils.Tokenizer(Exception("I am a silly cat"))
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)  

if __name__ == '__main__':
    unittest.main()