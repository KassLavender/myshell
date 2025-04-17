class myProgram:
    """Program object."""
    def __init__(self):
        self.manual = self.__doc__
    
    def help(self) -> list[str]:
        for line in self.manual:
            print(line)



class binaryToIntegerProgram(myProgram):
    """In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100.
    
    When given a string of binary values, outputs the decimal integer that would be represented in Python."""
    def __init__(self):
        self.name = "binaryToInteger"

        self.prompt = "Enter binary integer: "

        self.operation = self.binaryToInteger

        super().__init__()

    def binaryToInteger(self, integerStr: str | int) -> int:

        sign = 1

        try:
            bitList = [int(x) for x in str(integerStr)]
        except:
            raise ValueError("Not an integer.")

        try:
            match bitList[0]:
                case 0: sign = 0
                case 1: sign = 1
                case _: raise ValueError("Not a binary integer.")

            for i in range(len(bitList)):
                match int(bitList[i]):
                    case 0: bitList[i] = "1"
                    case 1: bitList[i] = "0"
                    case _: raise ValueError("Not a binary integer.")
        except Exception as e:
            raise e

        match (int(sign)):
            case 0: return (int("".join(bitList), 2) - 1)
            case 1: return -(int("".join(bitList), 2) + 1)



class integerToBinaryProgram(myProgram):
    """"In order to allow bit-wise operations, python represents negative integers e.g. -4 as 111....11100.
    
    When given a decimal integer, outputs the binary integer that would be represented in Python."""
    def __init__(self):
        self.name = "integerToBinary"

        self.prompt = "Enter decimal integer: "

        self.operation = self.integerToBinary

        super().__init__()
    
    def integerToBinary(self, integerStr: str | int) -> int:
        
        bitList = []
        sign = 0
        try:
            userInt = int(integerStr)
            if userInt < 0:
                sign = 1
                userInt = -userInt
        except:
            raise ValueError("Not an integer.")
        
        try:
            while userInt > 0:
                if (userInt % 2):
                    bitList.insert(0, 1)
                    userInt = (userInt - 1) / 2
                else:
                    bitList.insert(0, 0)
                    userInt = userInt / 2
            bitList.insert(0, sign)
        except:
            raise ValueError("Unexpected error.")

        return int(''.join(str(x) for x in bitList))
