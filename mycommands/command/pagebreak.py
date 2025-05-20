from mycommands import MyCommand



class PageBreak(MyCommand):
    """Prints a long line and then moves to the next line of the terminal.
    
    :param str name: `"PageBreak"`"""

    name = "PageBreak"

    def __init__(self):
        """Creates a PageBreak object.
        
        :param classmethod operation: points to `self.PageBreak`."""
        self.operation = self.PageBreak

    def PageBreak(self):
        try:
            print("—————————————————————————————")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with \"PageBreak\": {e}")
