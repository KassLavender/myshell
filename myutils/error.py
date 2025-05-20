class Error:
    """Exception handling utility. Prints the associated Exception(s)."""
    def __init__(self, *args: Exception):
        """When initialized, formats given :class:`Exception`s to a list, then automatically prints using :method:`Error.print`.
        
        :param list storedExceptions: takes gives `Exception`s, and formats them to be a clear message.
        :param classmethod operation: linked to `Error.print`."""
        assert all(isinstance(arg, Exception) for arg in args), "Cannot store Non-Exception object."
            
        self.storedExceptions = []
        self.operation = self.print

        try:
            for arg in args:
                self.storedExceptions.append(f"There was a problem executing the program: {arg}")
            self.print()
        except Exception as e:
            raise Exception(f"An unexpected error occurred with the Error handler instantiation: {e}")

    def print(self):
        """Called automatically with :classmethod:"""
        try:
            for error in self.storedExceptions:
                print(error)
        except Exception as e:
            raise Exception(f"An unexpected error occurred with Error handler print function: {e}")
        