# myshell
Simple shell terminal created as my project for learning Python and github. Meow!

### Available Programs:
**BinaryMaskToDecimal:**
In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
When given a string of binary values, outputs the decimal integer that would be represented in Python after demasking.
    
The first bit in the string of binary values denotes the sign (0 is positive, 1 is negative).

**DecimalToBinaryMask:**
In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
When given a decimal integer, outputs the string of binary values that would be represented in Python after masking up towards the nearest 2^x bytes (1 byte, 2 bytes, 4 bytes, etc).
    
The first bit denotes the sign (0 is positive, 1 is negative).

### Available Commands:
**ListAll:**
Lists all available programs and commands currently available.

Clears the terminal beforehand for legibility.
**ClearTerminal:**
Clears the terminal. Works on posix and nt-like systems.

**PageBreak**
"""Prints a long line and then moves to the next line of the terminal."""

### Utilities:
**Error:**
Exception handling utility. Prints the associated exception(s).

**OutputExtractor**
"""Captures operation print output for a stored class.
    
For situations when the output needs to be comparable or hidden, such as during unit testing."""

### Other Features:
Implements robust unittesting for all commands, programs, and utilities. /tests/test.py runs all tests.
