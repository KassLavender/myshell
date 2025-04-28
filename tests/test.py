#!/opt/homebrew/bin/python3.13

import unittest

from context import *
import tests



myTests = {}
loader = unittest.TestLoader()
for t in tests.__all__:
    myTests[t] = loader.loadTestsFromName(t)

testRunner = unittest.runner.TextTestRunner()

for t in myTests:
    print(t)
    testRunner.run(myTests[t])
    print()

# Somehow bring in every test_* class in the tests folder.
# Run test_outputextractor first.
    # If that is successful, run test_error.
        # If that is successful, run everything else.
# Running in this dependency order prevents the other tests (which rely on these util classes) from outputting duplicate errors relating to the utils.



