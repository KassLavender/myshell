import subprocess
from os import name as os_name

class MyCommand:
    """A command."""
    def __init__(self):
        self.manual = self.__doc__
    
    def help(self) -> print:
        try:
            print(self.manual)
        except Exception as e:
            raise Exception(f"An unexpected error occurred with printing help info: {e}")



class ClearTerminal(MyCommand):
    """Clears the terminal. Works on posix and nt-like systems."""
    name = "Clear"
    aliases = ["cls"]

    def __init__(self):
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
                self.run('cls', shell = True)
            else:
                self.run("clear")
        except Exception as e:
            raise Exception(f"An unexpected error occurred with ClearTerminal: {e}")



class PageBreak(MyCommand):
    """Prints a long line and then moves to the next line of the terminal."""

    name = "PageBreak"

    def __init__(self):
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
    name = "ListAll"
    aliases = ["list", "ls", "list all"]

    def __init__(self, programDict: dict = {}, commandDict: dict = {}):
        self.programNameSpace = {}
        self.commandNameSpace = {}

        # Make sure the input is dictionaries
        try:
            self.ProgramDict = dict(programDict)
            self.commandDict = dict(commandDict)
        except TypeError:
            raise TypeError("ListAll only accepts dict objects.")
        
        try:
            self.__assertCommandsAndPrograms()
            self.__buildNamespaces()
        except Exception as e:
            raise e
        
        self.operation = self.ListAll

        super().__init__()

    def __assertCommandsAndPrograms(self):
        # Make sure all programs have a .name string
        try:
            for prog in self.ProgramDict.values():
                assert isinstance(prog.name, str), "Program class name is not a string."
        except AttributeError:
            raise AttributeError("Program classes must have a name.")                
        
        # Make sure all commands that are tied to a class have a .name string.
        try:
            for com in filter(None, self.commandDict.values()):
                assert isinstance(com.name, str), "Command class name is not a string."
                
                # Should there be optional aliases, they must be a list of strings.
                try:
                    aliases = com.aliases
                except:
                    continue
                else:
                    assert (isinstance(com.aliases, list)), "Command aliases is not a list."
                    assert all(isinstance(a, str) for a in com.aliases), "Command alias is not a string."
        except AttributeError:
            raise AttributeError("Command classes must have a name.")

    def __buildNamespaces(self):
        def addToNameSpace(d: dict, name: str, inputtedClass: classmethod):
            if name.lower() in d:
                raise ValueError(f"Duplicate name or alias: \"{name.lower()}\" already in dictionary.")
            d[name.lower()] = inputtedClass

        try:
            # Associates [class].name and [class].aliases with the program or command class in a namespace.

            # Program classes have names.
            for prog in self.ProgramDict.values():
                addToNameSpace(self.programNameSpace, prog.name, prog)

            # Command classes have names, and maybe aliases.
            for com in filter(None, self.commandDict.values()):
                addToNameSpace(self.commandNameSpace, com.name, com)
                try:
                    for a in com.aliases:
                        addToNameSpace(self.commandNameSpace, a, com)
                except:
                    continue
        # addToNameSpace refuses to put duplicate keys into dictionary.
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"An unexpected error occured with ListAll.findCommand(): {e}")

    def ListAll(self) -> print:
            try:
                if self.ProgramDict:
                    print("Available programs:")
                    for i in self.ProgramDict.keys():
                        print(f" {str(i)}: {self.ProgramDict[i].name}")

                if self.ProgramDict and self.commandDict:
                    print()

                if self.commandDict:
                    print("Available commands:")
                    for i in self.commandDict.keys():
                        print(f" {str(i)}")
            except Exception as e:
                raise Exception(f"An unexpected error occurred with \"ListAll\": {e}")

    def findProgram(self, searchStr: str) -> classmethod | None:
        try:
            if searchStr.lower() in self.ProgramDict:
                return self.ProgramDict[searchStr.lower()]
            elif searchStr.lower() in self.programNameSpace:
                return self.programNameSpace[searchStr.lower()]
            else:
                return None
        except Exception as e:
            raise Exception(f"An unexpected error occurred with ListAll.findProgram(): {e}")
        
    def findCommand(self, searchStr: str) -> classmethod | None:
        try:
            if searchStr.lower() in self.commandDict:
                return self.commandDict[searchStr.lower()]
            elif searchStr.lower() in self.commandNameSpace:
                return self.commandNameSpace[searchStr.lower()]
            else:
                return None
        except Exception as e:
            raise Exception(f"An unexpected error occured with ListAll.findCommand(): {e}")
    
    def getHelp(self, searchStr: str) -> print:
        if (prog := self.findProgram(searchStr)) != None:
            prog.help()
            
        elif (com := self.findCommand(searchStr)) != None:
            com.help()

        elif searchStr in ["help", "info"]:
            print("Runs a program or command's inherited .help() method to print out the associated class's doc string.",
            "\n\nType \"help\" preceeded by a command, program, or progam number to instantly print its help info.",
            "\nEx:",
            "\n>>> help clear",
            "\nClears the terminal. Works on posix and nt-like systems.")

        elif searchStr in ["quit", "exit"]:
            print("Exits the terminal.")

        else:
            print("Command or program not found.")
