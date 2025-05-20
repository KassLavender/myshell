from io import StringIO
from contextlib import redirect_stdout



class OutputExtractor:
    """Captures operation print output for a stored class.
    
    For situations when the output needs to be comparable or hidden, such as during unit testing."""
    def __init__(self, givenClass: classmethod):
        """Initializes the OutputExtractor. Requires a given program or command or util with an `operation` method.
        
        :param classmethod storedClass: stores the :classmethod:`givenClass` object.
        
        :param classmethod operation: points to the stored class's `operation` method."""
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