#!/opt/homebrew/bin/python3.13

from mycommands import mycommands
from myprograms import myprograms
from myutils import myutils


programDictionary = {
    "1": myprograms.BinaryMaskToDecimalProgram(),
    "2": myprograms.DecimalToBinaryMaskProgram()
}

commandDictionary = {
    "list": mycommands.ListAll({},{}),
    "clear": mycommands.ClearTerminal()
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



while (userInput := input("\n" + "Type a command or program number: ")) not in {"quit", "exit"}:
    try:
        userInput = userInput.lower()
        PageBreakCommand.operation()
        print()

        match userInput:    
            case "help" | "info":
                print()

                #prompt a command or program number, uses .help()
            
            case "list" | "ls" | "list all" | "list" | "listall":
                ClearTerminalCommand.operation()
                ListAllCommand.operation()
                PageBreakCommand.operation()

            case "clear" | "cls":
                ClearTerminalCommand.operation()

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
        myutils.Error(e)