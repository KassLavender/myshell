class myProgram:
    """Program object."""
    def __init__(self):
        self.manual = self.__doc__
    
    def help(self) -> list[str]:
        for line in self.manual:
            print(line)



class binaryMaskToDecimalProgram(myProgram):
    """In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
    When given a string of binary values, outputs the decimal integer that would be represented in Python after demasking.
    
    The first bit in the string of binary values denotes the sign (0 is positive, 1 is negative)."""
    def __init__(self):
        self.name = "binaryMaskToDecimal"

        self.prompt = "Enter a binary integer, prefaced with a signing bit (0 is positive): "

        self.operation = self.binaryMaskToDecimal

        super().__init__()

    def binaryMaskToDecimal(self, integerStr: str | int) -> int:
        sign = 1

        try:
            bitList = [int(i) for i in str(integerStr)]
        except:
            raise ValueError("Not an integer.")

        try:
            match bitList[0]:
                case 0: sign = 0
                case 1: sign = 1
                case _: raise ValueError("Not a binary integer.")

            for i in range(len(bitList)):
                if sign == 1:
                    # Flip bits for negative binary masks.
                    match int(bitList[i]):
                        case 0: bitList[i] = "1"
                        case 1: bitList[i] = "0"
                        case _: raise ValueError("Not a binary integer.")
                else:
                    match int(bitList[i]):
                        case 0: bitList[i] = "0"
                        case 1: bitList[i] = "1"
                        case _: raise ValueError("Not a binary integer.")

            # Converts bitList into a decimal integer.
            match (int(sign)):
                case 0: return (int("".join(bitList), 2))
                # Add 1 for two's complement.
                case 1: return -(int("".join(bitList), 2) + 1)
                case _: raise Exception("Unexpected casing error.")
        except Exception as e:
            raise e




class decimalToBinaryMaskProgram(myProgram):
    """"In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100, where 100 is equivalent to 11100 and so forth.
    
    When given a decimal integer, outputs the string of binary values that would be represented in Python after masking.
    
    The first bit denotes the sign (0 is positive, 1 is negative)."""
    def __init__(self):
        self.name = "decimalToBinaryMask"

        self.prompt = "Enter a decimal integer: "

        self.operation = self.decimalToBinaryMask

        super().__init__()
    
    def decimalToBinaryMask(self, integerStr: str | int) -> str:  
        bitList = []
        sign = 0

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
                    userInt = (userInt - 1) / 2
                else:
                    bitList.insert(0, 0)
                    userInt = userInt / 2
            
            # Flips bits for negative numbers.
            if sign == 1:
                for i in range(len(bitList)):
                    match bitList[i]:
                        case 1: bitList[i] = 0
                        case 0: bitList[i] = 1

            # Inserts the case-signifying bit.
            bitList.insert(0, sign)

            # Has to be a string, as positive binary integers are prefaced with 0.
            return ''.join(str(x) for x in bitList)
        except:
            raise Exception("Unexpected calculation error.")
