from io import StringIO
from contextlib import redirect_stdout



class Error:
    """Exception handling utility. Prints the associated exception(s).

    .__init__(*args:Exception): Formats given Exception arguments as a message, then redirects to print().
    
    .print(): Prints all stored Exceptions."""
    def __init__(self, *args: Exception):
        assert all(isinstance(arg, Exception) for arg in args), "Cannot store Non-Exception object."
            
        self.storedExceptions = []
        self.operation = self.print

        try:
            for arg in args:
                self.storedExceptions.append(f"There was a problem executing the program: {arg}")
            self.print()
        except Exception as e:
            raise Exception(f"An unexpected error occurred with the Error handler instantiation: {e}")

    def print(self) -> print:
        try:
            for error in self.storedExceptions:
                print(error)
        except Exception as e:
            raise Exception(f"An unexpected error occurred with Error handler print function: {e}")
        


class OutputExtractor:
    """Captures operation print output for a stored class.
    
    For situations when the output needs to be comparable or hidden, such as during unit testing."""
    def __init__(self, givenClass: classmethod):
        assert hasattr(givenClass, 'operation'), "Given object has no .operation() method."
        
        self.storedClass = givenClass
        self.operation = self.storedClass.operation
    
    def getOutput(self, methodStr: str = None, *methodStrArgs) -> str:
        """Defaults to running the .operation method of the stored class.
        
        If given the name of a different method, will attempt to run that method instead, with any passed arguments."""
        try:
            # Create StringIO object.
            redirected = StringIO()

            # Capture the method output.
            with redirect_stdout(redirected):
                if methodStr == None:
                    self.storedClass.operation()
                else:
                    getattr(self.storedClass, methodStr)(*methodStrArgs)

            # Turn that IO object into a comparable string.
            return redirected.getvalue()
        except AttributeError as e:
            raise AttributeError(f"\"{type(self.storedClass).__name__}\" has no method \"{methodStr}\".")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with the OutputExtractor output function: {e}")



def Tokenizer(userInput: str) -> list[str]:
    """Turns a string with spaces into a list of strings.
    Removes empty words in case of superfluous spaces."""
    assert isinstance(userInput, str), "Tokenizer can only accept a string as input."
    try:
        processed = userInput.split()
        processed = list(filter(None, processed))
        return processed
    except Exception as e:
        raise Exception(f"An unexpected error occurred with the input tokenizer: {e}")



def Helper(inputList: list[str]) -> str:
    """Manager for pulling help info.
    If the inputList length is 1, asks for a particular name of a command or program.
    If the length is 2, the second "word" must be the name of the command or program itself.
    If the length is any longer, trims everything beyond the second "word", and runs itself with length 2."""
    assert isinstance(inputList, list), "Helper can only accept a list of words as input."
    assert all(isinstance(a, str) for a in inputList), "Helper can only accept a list of words as input."
    try:
        match len(inputList):
            case 0:
                return None
            case 1:
                helpInput = input("With what command or program?:\n>>> ")
                print()
                return helpInput
            case 2:
                return inputList[1].lower()
            case _:
                return Helper(inputList[:2])
    except Exception as e:
        raise Exception(f"An unexpected error occurred with the helper util: {e}")
