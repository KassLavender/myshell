"""Shell program.

Lets users run programs and commands, which looks pretty on terminals.

Works on POSIX and NT systems. Go to https://github.com/KassLavender/myshell for any additional help."""

#!/usr/bin/env python3.13
import sys

from mycommands import mycommands
from myprograms import myprograms
from myutils import myutils

#Lets inputted numbers be longer than 4300 digits.
sys.set_int_max_str_digits(0)


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
        inputList = myutils.Tokenizer(userInput)
        PageBreakCommand.operation()
        print()

        if len(inputList) == 0:
            continue

        match inputList[0]:    
            case "help" | "info" | "h" | "i":
                helpInput = myutils.Helper(inputList)
                ListAllCommand.getHelp(helpInput.lower())

            
            case "list" | "ls" | "list all" | "list" | "listall":
                ClearTerminalCommand.operation()
                ListAllCommand.operation()
                PageBreakCommand.operation()
                continue

            case "clear" | "cls":
                ClearTerminalCommand.operation()

            case "quit" | "exit":
                raise SystemExit

            case _:
                program = ListAllCommand.findProgram(inputList[0])

                if program:
                    programArgument = input(program.prompt)
                    print()
                    print(program.operation(programArgument))
                else:
                    print("Not a command nor program.")
            
                

                
        PageBreakCommand.operation()
    except Exception as e:
        myutils.Error(e)