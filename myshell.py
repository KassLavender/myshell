#!/usr/bin/env python3.13

from mycommands import mycommands
from myprograms import myprograms
from myutils import myutils


programDictionary = {
    "1": myprograms.BinaryMaskToDecimalProgram(),
    "2": myprograms.DecimalToBinaryMaskProgram()
}

commandDictionary = {
    "ListAll": mycommands.ListAll(),
    "clear": mycommands.ClearTerminal(),
    "help": None,
    "exit": None
}



try:
    ClearTerminalCommand = mycommands.ClearTerminal()
    ListAllCommand = mycommands.ListAll(programDictionary, commandDictionary)
    PageBreakCommand = mycommands.PageBreak()

    ClearTerminalCommand.operation()
    ListAllCommand.operation()
    PageBreakCommand.operation()
except Exception as e:
    myutils.Error(e)
    quit()



while (userInput := input("\nType a command, program, or program number:\n>>> ")) not in {"quit", "exit"}:
    try:
        userInput = userInput.lower()
        PageBreakCommand.operation()
        print()

        match userInput:    
            case "help" | "info":
                helpInput = input("With what command or program?:\n>>> ")
                print()
                ListAllCommand.getHelp(helpInput.lower())

            
            case "list" | "ls" | "list all" | "list" | "listall":
                ClearTerminalCommand.operation()
                ListAllCommand.operation()
                PageBreakCommand.operation()
                continue

            case "clear" | "cls":
                ClearTerminalCommand.operation()

            case _:

                if userInput.startswith(prefix := ("help ", "h ")):
                    userInput = userInput.removeprefix("help ")
                    # Not yet implemented
                    continue


                program = ListAllCommand.findProgram(userInput)

                if program != None:
                    programArgument = input(program.prompt)
                    print()
                    print(program.operation(programArgument))
                else:
                    print("Not a command nor program.")
            
                

                
        PageBreakCommand.operation()
    except Exception as e:
        myutils.Error(e)