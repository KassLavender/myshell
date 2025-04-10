import os

class myCommand:
    """A command."""
    def __init__(self):
        self.manual = self.__doc__

    def help(self) -> print:
        for line in self.manual:
            try:
                print(line)
            except:
                raise Exception("An unexpected error occured with printing \"help\".")



class clearTerminal(myCommand):
    """Clears the terminal."""

    def __init__(self):
        self.name = "clear"

        self.operation = self.clearTerminal

        super().__init__()

    def clearTerminal(self):
        try:
            os.system('cls||clear')
        except:
            raise Exception("An unexpected error occurred with clearTerminal.")



class pageBreak(myCommand):
    """Prints a long line and then moves to the next line of the terminal."""

    def __init__(self):
        self.name = "pageBreak"
        
        self.operation = self.pageBreak

        super().__init__()

    def pageBreak(self) -> print:
        try:
            print("—————————————————————————————")
        except:
            raise Exception("An unexpected error occurred with \"pageBreak\".")



class listAll(myCommand):
    """Lists all available programs and commands currently available.
    
    Clears the terminal beforehand for legibility."""
    def __init__(self, programMap: map, commandMap: map):
        self.name = "listAll"

        self.programMap = programMap

        self.commandMap = commandMap

        self.operation = self.listAll

        super().__init__()
    
    def listAll(self) -> print:
            try:
                print("Available programs:")
                for i in self.programMap.keys():
                    print(f" {str(i)}: {self.programMap[i].name}")

                print("\n" + "Available commands:")
                for i in self.commandMap.keys():
                    print(f" {self.commandMap[i].name}")
                
                pageBreak().operation()
            except:
                raise Exception("An unexpected error occurred with \"listAll\".")
