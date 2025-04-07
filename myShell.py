#!/opt/homebrew/bin/python3.13

import os

from myPrograms import myPrograms


myCommands = ["help", "list", "quit or exit"]

programMap = {
    "1": myPrograms.binaryToNumberProgram(),
    "2": myPrograms.numberToBinaryProgram()
}


def clear():
    """Clear the terminal."""
    os.system('cls||clear')

def pageBreak():
    """prints a long line and then moves to the next line of terminal."""
    print("—————————————————————————————")


def listAll():
    """Lists available programs and commands in this program."""
    print("Available programs:")
    for i in programMap.keys():
        print (" " + str(i) + ": " + programMap[i].name)

    print("\n" + "Available commands:")
    for i in range(len(myCommands)):
        print (" " + myCommands[i])
    pageBreak()


clear()
listAll()






while (userInput := input("\n" + "Type a command or program number: ")) not in {"quit", "exit"}:

    userInput = userInput.lower()
    pageBreak()
    print()

    match userInput:
        case "help" | "info":
            print("Type \"[command].help\" or \"[program].help\" for info.")
        
        case "list" | "ls":
            clear()
            listAll()

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
