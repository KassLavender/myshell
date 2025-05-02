from io import StringIO
from contextlib import redirect_stdout



class Error:
    """Error utility. Prints the associated exception(s).

    .__init__(*args:Exception): Formats given Exception arguments as a message, then redirects to print().
    
    .print(): Prints all stored Exceptions."""
    def __init__(self, *args: Exception):
        for arg in args:
            if not isinstance(arg, Exception):
                raise ValueError("Cannot store Non-Exception object.")
            
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
        if hasattr(givenClass, 'operation') is False:
            raise AttributeError("Given object has no .operation() method.")
        
        self.storedClass = givenClass
        self.operation = self.storedClass.operation
    
    def getOutput(self) -> str:
        try:
            # Create StringIO object.
            redirected = StringIO()

            # Capture the method output.
            with redirect_stdout(redirected):
                self.storedClass.operation()

            # Turn that IO object into a comparable string.
            return redirected.getvalue()
        except Exception as e:
            raise Exception(f"An unexpected error occurred with the OutputExtractor output function: {e}")
