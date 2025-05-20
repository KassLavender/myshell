from mycommands import MyCommand
from myprograms import MyProgram



class ListAll(MyCommand):
    """Lists all available programs and commands currently available.

    Clears the terminal beforehand for legibility.
    
    :param str name: `ListAll`
    :param list aliases: `["list", "ls", "list all"]`"""
    name = "ListAll"
    aliases = ["list", "ls", "list all"]

    def __init__(self, programDict: dict = {}, commandDict: dict = {}):
        """Builds namespaces for given dictionaries of programs and commands.
        
        :param dict programDict: Stores the given `programDict` dictionary.
        :param dict commandDict: Stores the given `commandDict` dictionary.
        :param dict programNameSpace: All `name`s of programs are tied to the programs themselves and are therefore callable using the `name`s.
        :param dict commandNameSpace: Same as for programs, but also including `aliases` of commands.
        :param classmethod _assertCommandsAndPrograms: Makes sure given `programDict` and `commandDict` dictionaries have commands and programs of the correct format to be processed by the namespaces.
        :param classmethod _buildNameSpace: Builds the namespace dictionaries using the given 'programDict' and 'commandDict' dictionaries.
        :param classmethod operation: Points to `self.ListAll`."""
        self.programNameSpace = {}
        self.commandNameSpace = {}

        # Make sure the input is dictionaries
        try:
            self.programDict = dict(programDict)
            self.commandDict = dict(commandDict)
        except TypeError:
            raise TypeError("ListAll only accepts dict objects.")
        
        try:
            self.__assertCommandsAndPrograms()
            self.__buildNamespaces()
        except Exception as e:
            raise e
        
        self.operation = self.ListAll

    def __assertCommandsAndPrograms(self):
        """Called automatically through the :method:`__init__` process.
        
        Makes sure that all programs and commands have `name`s of the proper format, and if commands have `aliases` that they are of the proper format."""
        # Make sure all programs have a .name string
        try:
            for prog in self.programDict.values():
                assert isinstance(prog.name, str), "Program class name is not a string."
        except AttributeError:
            raise AttributeError("Program classes must have a name.")                
        
        # Make sure all commands that are tied to a class have a .name string.
        try:
            for com in filter(None, self.commandDict.values()):
                assert isinstance(com.name, str), "Command class name is not a string."
                
                # Should there be optional aliases, they must be a list of strings.
                if hasattr(com, "aliases"):
                    assert (isinstance(com.aliases, list)), "Command aliases is not a list."
                    assert all(isinstance(a, str) for a in com.aliases), "Command alias is not a string."
        except AttributeError:
            raise AttributeError("Command classes must have a name.")

    def __buildNamespaces(self):
        """Called automatically through the :method:`__init__` process.
        
        Builds the namespace dictionaries from the program's `commandDict` and `programDict` dictionaries."""
        def addToNameSpace(d: dict, inputtedName: str, inputtedClass: classmethod):
            name = inputtedName.lower()
            # addToNameSpace refuses to put duplicate keys into dictionary.
            if name in d:
                raise ValueError(f"Duplicate name or alias: \"{name}\" already in dictionary.")
            d[name] = inputtedClass

        try:
            # Associates [class].name and [class].aliases with the program or command class in a namespace.

            # Program classes have names.
            for prog in self.programDict.values():
                addToNameSpace(self.programNameSpace, prog.name, prog)

            # Command classes have names, and maybe aliases.
            for com in filter(None, self.commandDict.values()):
                addToNameSpace(self.commandNameSpace, com.name, com)
                if hasattr(com, "aliases"):
                    for a in com.aliases:
                        addToNameSpace(self.commandNameSpace, a, com)
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"An unexpected error occured with ListAll.findCommand(): {e}")

    def ListAll(self):
            """Prints all programs and commands in `programDict` and `commandDict` to terminal, formatted for readability."""
            try:
                if self.programDict:
                    print("Available programs:")
                    for i in self.programDict.keys():
                        print(f" {str(i)}: {self.programDict[i].name}")

                if self.programDict and self.commandDict:
                    print()

                if self.commandDict:
                    print("Available commands:")
                    for i in self.commandDict.keys():
                        print(f" {str(i)}")
            except Exception as e:
                raise Exception(f"An unexpected error occurred with \"ListAll\": {e}")

    def findProgram(self, inputtedSearchStr: str) -> MyProgram | None:
        """Finds a program by name in `programDict` or in the program namespace. If found, returns that program."""
        try:
            searchStr = inputtedSearchStr.lower()
            if searchStr in self.programDict:
                return self.programDict[searchStr]
            elif searchStr in self.programNameSpace:
                return self.programNameSpace[searchStr]
            else:
                return None
        except Exception as e:
            raise Exception(f"An unexpected error occurred with ListAll.findProgram(): {e}")
        
    def findCommand(self, inputtedSearchStr: str) -> MyCommand | None:
        """Finds a command by name in `commandDict` or in the command namespace. If found, returns that command."""
        try:
            searchStr = inputtedSearchStr.lower()
            if searchStr in self.commandDict:
                return self.commandDict[searchStr]
            elif searchStr in self.commandNameSpace:
                return self.commandNameSpace[searchStr]
            else:
                return None
        except Exception as e:
            raise Exception(f"An unexpected error occured with ListAll.findCommand(): {e}")
        
    def getHelp(self, searchStr: str):
        """Takes a search string, and tries to find a program or command with that particular name. Then, uses the program or class's `help` method to print the information to the terminal.
        
        Also contains help information for "help" or "quit", which are pseudocommands for :module:`myshell`.
        
        Otherwise, states that the command or program was not found."""
        if (prog := self.findProgram(searchStr)):
            prog.help()
            
        elif (com := self.findCommand(searchStr)):
            com.help()

        elif searchStr in ["help", "info"]:
            print("Runs a program or command's inherited .help() method to print out the associated class's doc string.",
            "\n\nType \"help\" followed by a command, program, or progam number to instantly print its help info.",
            "\nEx:",
            "\n>>> help clear",
            "\nClears the terminal. Works on posix and nt-like systems.")

        elif searchStr in ["quit", "exit"]:
            print("Exits the terminal.")

        else:
            print("Command or program not found.")
