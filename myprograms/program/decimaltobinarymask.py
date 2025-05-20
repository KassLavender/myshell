from myprograms import MyProgram



class DecimalToBinaryMaskProgram(MyProgram):
    """"In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
    When given a decimal integer, outputs the string of binary values that would be represented in Python after masking up towards the nearest 2^x bytes (1 byte, 2 bytes, 4 bytes, etc).
    
    The first bit denotes the sign (0 is positive, 1 is negative).
    
    :param str name: `DecimalToBinaryMask`"""
    name = "DecimalToBinaryMask"

    def __init__(self):
        """Initializes the program.

        :param str prompt: Asks for a decimal integer.
        :param classmethod operation: links to `Self.DecimalToBinaryMask`."""
        self.prompt = "Enter a decimal integer:\n>>> "

        self.operation = self.DecimalToBinaryMask
    
    def DecimalToBinaryMask(self, integerStr: str | int) -> str:
        """Interprets a given decimal integer, and returns the associated binary mask."""  
        bitList = []
        sign = 0

        # Internal bit-masking function. Inserts case-signifying bit(s).
        def mask(num: int):
            for _ in range(num):
                bitList.insert(0,sign)

        # Internal mathematic function. Finds the next power of 2 given a number.
        next_power_of_2 = lambda n: 2**(n - 1).bit_length()

        # Internal mathematic function. 0 and 1 become the other.
        flipBit = lambda b: (b + 1) % 2

        try:
            userInt = int(integerStr)
            if userInt < 0:
                sign = 1
                # Two's complement for negative decimal integers.
                userInt = -userInt - 1
        except:
            raise ValueError("Not an integer.")
        
        try:
            # Converts the decimal number into a binary list.
            while userInt > 0:
                if (userInt % 2):
                    bitList.insert(0, 1)
                    userInt = (userInt - 1) // 2
                else:
                    bitList.insert(0, 0)
                    userInt = userInt // 2
                    
            # Flips bits for negative numbers.
            if sign == 1:
                bitList = list(map(flipBit, bitList))
            
            # Masks up to nearest byte.
            mod = len(bitList) % 8
            if 8 - mod == 0:
                mask(8)
            else:
                mask(8-mod)
            
            # Masks up to nearest integer power of two number of bytes.
            bytes = int(len(bitList) // 8)
            bytesToNextPower = next_power_of_2(bytes) - bytes
            mask(8*bytesToNextPower)

            # Has to be a string, as positive binary integers are prefaced with 0.
            return ''.join(str(x) for x in bitList)
        except Exception as e:
            raise e
