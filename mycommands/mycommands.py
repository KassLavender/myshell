from subprocess import run as subprocess_run

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
    """Clears the terminal."""

    def __init__(self):
        self.name = "clear"

        self.operation = self.ClearTerminal

        super().__init__()

    def run(self, arg, shell=False):
        subprocess_run(arg,shell=shell)

    def ClearTerminal(self):
        try:
            self.run("clear||cls", shell=True)
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
            raise TypeError("ListAll only accepts map objects.")

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
