#!/opt/homebrew/bin/python3.13

from myprograms import myprograms
from mycommands import mycommands
from myutils import myutils


programDictionary = {
    "1": myprograms.binaryMaskToDecimalProgram(),
    "2": myprograms.decimalToBinaryMaskProgram()
}

commandDictionary = {
    "list": mycommands.listAll({},{}),
    "clear": mycommands.clearTerminal()
}



try:
    clearTerminalCommand = mycommands.clearTerminal()
    listAllCommand = mycommands.listAll(programDictionary, commandDictionary)
    pageBreakCommand = mycommands.pageBreak()

    clearTerminalCommand.operation()
    listAllCommand.operation()
except Exception as e:
    myutils.error(e)



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
        myutils.error(e)