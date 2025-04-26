import io
from contextlib import redirect_stdout

def error(e: Exception) -> print:
    """Error utility. Prints the associated exception."""
    print(f"There was a problem executing the program: {e}")



def exceptionOutputExtraction(e: Exception) -> str:
    """Exception handling utility. Returns exception output converted to a string."""
    # Create StringIO object.
    newOutput = io.StringIO()

    # Capture the error utility output.
    with redirect_stdout(newOutput):
        error(e)
    
    # Turn that IO object into a comparable string.
    return newOutput.getvalue()

