#!/opt/homebrew/bin/python3.13

import io
import unittest
from contextlib import redirect_stdout

from context import myutils



error = Exception



class test_error(unittest.TestCase):

    def test_error(self):
        try:

            answerStr = "There was a problem executing the program: <class 'Exception'>\n"

            # Create StringIO object.
            errorUtilOutput = io.StringIO()
            
            # Capture the error utility output.
            with redirect_stdout(errorUtilOutput):
                myutils.error(error)
            
            # turn that IO object into a comparable string.
            errorStr = errorUtilOutput.getvalue()

            # Compare the ideal error output with the error util output.
            self.assertEqual(answerStr, errorStr)

        except Exception as e:
            print("There was a problem with creating a problem to be displayed by the error utility.")
            myutils.error(e)

if __name__ == '__main__':
    unittest.main()