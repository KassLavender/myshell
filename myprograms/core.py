import re



class MyProgram:
    """Program object."""
    @classmethod    
    def help(command):
        """Prints the `__doc__` string of the class.
        
        First cleans out any backtick marks, and `ReST`-type dockstring lines."""
        try:
            help = re.sub("`", "", command.__doc__)
            help = re.sub(r":param \w* ", "", help)
            print(help)
        except Exception as e:
            raise Exception(f"An unexpected error occurred with printing help info: {e}")   