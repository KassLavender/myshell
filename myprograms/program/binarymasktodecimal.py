from myprograms import MyProgram



class BinaryMaskToDecimalProgram(MyProgram):
    """In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
    When given a string of binary values, outputs the decimal integer that would be represented in Python after demasking.
    
    The first bit in the string of binary values denotes the sign (0 is positive, 1 is negative).
    
    :param str name: `BinaryMaskToDecimal`"""
    name = "BinaryMaskToDecimal"

    def __init__(self):
        """Initializes the program.

        :param str prompt: Prompt asking for a binary mask.
        :param classmethod operation: links to `Self.BinaryMaskToDecimal`.
        """
        self.prompt = "Enter a binary integer, prefaced with a signing bit (0 is positive):\n>>> "

        self.operation = self.BinaryMaskToDecimal

    def BinaryMaskToDecimal(self, integerStr: str | int) -> int:
        """Interprets a given string of 0s and 1s in the format of a binary mask, and returns the associated decimal integer."""
        sign = 1

        # Internal mathematic function. 0 and 1 become the other.
        flipBit = lambda b: (b + 1) % 2

        try:
            bitList = [int(i) for i in str(integerStr)]
        except:
            raise ValueError("Not an integer.")
        else:
            # Checks if there's any values in the list that aren't 0 or 1
            if list(filter(lambda x: x not in [0,1], bitList)):
                raise ValueError("Not a binary integer.")

        try:
            sign = bitList[0]

            # Flip bits for negative binary masks.
            if sign == 1:
                bitList = list(map(flipBit, bitList))
            
            bitList = list(map(str, bitList))

            # Converts bitList into a decimal integer.
            match sign:
                case 0: return (int("".join(bitList), 2))
                # Add 1 for two's complement.
                case 1: return -(int("".join((bitList)), 2) + 1)
        except Exception as e:
            raise e