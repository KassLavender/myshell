#!/usr/bin/env python3.13

import unittest

from context import *



keyTests = {}
remainingTests = {}
resultList = []
failures = False

loader = unittest.TestLoader()
testRunner = unittest.runner.TextTestRunner()

for t in tests.__keyTests__:
    keyTests[t] = loader.loadTestsFromName(t)

for t in tests.__remainingTests__:
    remainingTests[t] = loader.loadTestsFromName(t)



for t in keyTests:
    print(f"{t}:")
    result = testRunner.run(keyTests[t])
    if result.errors or result.failures:
        print("\nA utility test failed. Fix before remaining tests can be run.")
        exit(1)

for t in remainingTests:
        print(f"{t}:")
        result = testRunner.run(remainingTests[t])
        if result.errors or result.failures:
             failures = True

if failures:
     print("\nOne or more tests failed.")
     exit(1)

print("All tests successful.")
