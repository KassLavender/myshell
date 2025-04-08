#!/opt/homebrew/bin/python3.13

import os

from myPrograms import myPrograms
from myCommands import myCommands


programMap = {
    "1": myPrograms.binaryToIntegerProgram(),
    "2": myPrograms.integerToBinaryProgram()
}

commandMap = {
#    "1": myCommands.help(),
    "2": myCommands.listAll({},{}),
    "3": myCommands.clearTerminal(),
    "4": myCommands.pageBreak()
}

clearTerminalCommand = myCommands.clearTerminal()
listAllCommand = myCommands.listAll(programMap, commandMap)
pageBreakCommand = myCommands.pageBreak()



clearTerminalCommand.operation()
listAllCommand.operation()



while (userInput := input("\n" + "Type a command or program number: ")) not in {"quit", "exit"}:

    userInput = userInput.lower()
    pageBreakCommand.operation()
    print()

    match userInput:
        case "help" | "info":
            print()

            #prompt a command or program number, uses .help()
        
        case "list" | "ls" | "list all" | "list" | "listall":
            clearTerminalCommand.operation()
            listAllCommand.operation()

        case "pagebreak" | "break":
            pageBreakCommand.operation()

        case _:
                try:
                    if userInput not in programMap:
                        print ("Not a command nor program.")
                        continue

                except ValueError:
                    print("Unexpected error.")

                try:
                    programArgument = input(programMap[userInput].prompt)
                        
                    print(programMap[userInput].operation(programArgument))
                except Exception as e:
                    print (f"There was a problem executing the program: {e}")
