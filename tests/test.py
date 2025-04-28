#!/opt/homebrew/bin/python3.13

import unittest

from context import myutils, mycommands

from tests import *
#from tests import __all__



suite = unittest.defaultTestLoader.discover(test_error.__path__)




# Somehow bring in every test_* class in the tests folder.
# Run test_outputextractor first.
    # If that is successful, run test_error.
        # If that is successful, run everything else.
# Running in this dependency order prevents the other tests (which rely on these util classes) from outputting duplicate errors relating to the utils.



if __name__ == '__main__':

    unittest.TextTestRunner().run(suite)