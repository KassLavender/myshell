#!/opt/homebrew/bin/python3.13

import unittest

from context import myutils, mycommands

from tests import *
# from tests import __all__

def suite():
    suite = unittest.suite.TestSuite()
    suite.addTest(test_outputextractor('test_OutputExtractor'))
    suite.addTest(test_error('test_Error'))

# unittestList = []
# for i in __all__:
#     unittestList.append(i)
# test_error


#silly = test_error.test_Error

# Somehow bring in every test_* class in the tests folder.
# Run test_outputextractor first.
    # If that is successful, run test_error.
        # If that is successful, run everything else.
# Running in this dependency order prevents the other tests (which rely on these util classes) from outputting duplicate errors relating to the utils.



if __name__ == '__main__':
    runner = unittest.runner.TextTestRunner()
    runner.run(suite())