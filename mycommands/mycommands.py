import subprocess
from os import name as os_name

class MyCommand:
    """A command."""
    def __init__(self):
        self.manual = self.__doc__

    def help(self) -> print:
        try:
            for line in self.manual:
                print(line)
        except Exception as e:
            raise Exception(f"An unexpected error occured with printing help info: {e}")



class ClearTerminal(MyCommand):
    """Clears the terminal. Works on posix and nt-like systems."""

    def __init__(self):
        self.name = "clear"

        self.operation = self.ClearTerminal

        super().__init__()

    def getos_name(self):
        return os_name

    def run(self, arg, shell=False):
        subprocess.run(arg,shell=shell)

    # While "java" is registered in os.name, jython does not yet support python 3. So I'm not bothering with that.
    def ClearTerminal(self):
        try:
            if self.getos_name() == "nt":
                self.run("cls")
            else:
                self.run("clear")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with ClearTerminal: {e}")



class PageBreak(MyCommand):
    """Prints a long line and then moves to the next line of the terminal."""

    def __init__(self):
        self.name = "PageBreak"
        
        self.operation = self.PageBreak

        super().__init__()

    def PageBreak(self) -> print:
        try:
            print("—————————————————————————————")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with \"PageBreak\": {e}")



class ListAll(MyCommand):
    """Lists all available programs and commands currently available.
    
    Clears the terminal beforehand for legibility."""
    def __init__(self, programMap: map, commandMap: map):
        self.name = "ListAll"

        try:
            self.programMap = dict(programMap)
            self.commandMap = dict(commandMap)
        except:
            raise ValueError("ListAll only accepts map objects.")

        self.operation = self.ListAll

        super().__init__()
    
    def ListAll(self) -> print:
            try:
                if self.programMap:
                    print("Available programs:")
                    for i in self.programMap.keys():
                        print(f" {str(i)}: {self.programMap[i].name}")
                    print()
                if self.commandMap:
                    print("Available commands:")
                    for i in self.commandMap.keys():
                        print(f" {self.commandMap[i].name}")
            except Exception as e:
                raise Exception(f"An unexpected error occurred with \"ListAll\": {e}")
