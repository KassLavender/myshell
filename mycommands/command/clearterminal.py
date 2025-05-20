import subprocess
from os import name as os_name

from mycommands import MyCommand



class ClearTerminal(MyCommand):
    """Clears the terminal. Works on posix and nt-like systems.
    
    :param str name: `\"clear\"`
    :param lst aliases: `[\"cls\"]`"""
    name = "Clear"
    aliases = ["cls"]

    def __init__(self):
        """creates a ClearTerminal object.

        :param classmethod operation: set to `Clearterminal.ClearTerminal`
        """
        self.operation = self.ClearTerminal

    def getos_name(self):
        """Determines what operating system namespace is ClearTerminal being run on."""
        return os_name

    def run(self, arg, shell=False):
        """Allows processes to run commands in terminal with arguments."""
        subprocess.run(arg,shell=shell)

    # While "java" is registered in os.name, jython does not yet support python 3. So I'm not bothering with that.
    def ClearTerminal(self):
        """For nt and posix systems, attempts to run a clear terminal command through a subprocess."""
        try:
            if self.getos_name() == "nt":
                self.run('cls', shell = True)
            else:
                self.run("clear")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with ClearTerminal: {e}")
