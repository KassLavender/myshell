#!/opt/homebrew/bin/python3.13

from myPrograms import myPrograms
from myCommands import myCommands
from myUtils import myUtils


programDictionary = {
    "1": myPrograms.binaryToIntegerProgram(),
    "2": myPrograms.integerToBinaryProgram()
}

commandDictionary = {
    "list": myCommands.listAll({},{}),
    "clear": myCommands.clearTerminal()
}



try:
    clearTerminalCommand = myCommands.clearTerminal()
    listAllCommand = myCommands.listAll(programDictionary, commandDictionary)
    pageBreakCommand = myCommands.pageBreak()

    clearTerminalCommand.operation()
    listAllCommand.operation()
except Exception as e:
    myUtils.error(e)



while (userInput := input("\n" + "Type a command or program number: ")) not in {"quit", "exit"}:
    try:
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

            case "clear":
                clearTerminalCommand.operation()

            case _:
                try:
                    if userInput not in programDictionary:
                        print("Not a command nor program.")
                        continue

                except ValueError:
                    print("Unexpected error.")

                programArgument = input(programDictionary[userInput].prompt)
                print(programDictionary[userInput].operation(programArgument))

    except Exception as e:
        myUtils.error(e)