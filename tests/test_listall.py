#!/usr/bin/env python3.13

import unittest

from context import mycommands, myprograms, myutils



class test_ListAll(unittest.TestCase):    
    programDict = {
            "1": myprograms.BinaryMaskToDecimalProgram()
        }
    commandDict = {
            "clear": mycommands.ClearTerminal()
        }
    programAnswer = "Available programs:\n 1: BinaryMaskToDecimal\n"
    commandAnswer = "Available commands:\n clear\n"
    comboAnswer = programAnswer + "\n" + commandAnswer

    class TestProgram():
        name = "TestProgram"
    
    class TestProgramNameless():
        pass

    class TestProgramWeirdName():
        name = ["I", "am", "a", "silly", "cat"]

    class TestCommand():
        name = "TestCommand"

    class TestCommandNameless():
        pass

    class TestCommandWeirdName():
        name = Exception("I am a silly cat.")

    class TestCommandWithAliases():
        name = "TestCommand2"
        aliases = ["secondtest"]

    class TestCommandWeirdAliases():
        name = "TestCommandWeirdAliases"
        aliases = {"I am" : Exception("A silly cat")}
    
    class TestCommandWeirdAliasesString():
        name = "TestCommandWeirdAliasesString"
        aliases = ["I am a silly cat", 4]

    def createListAll(self, program: map, command: map) -> str:
        try:
            ListAll = mycommands.ListAll(program, command)
            return ListAll
        except Exception as e:
            raise e

    def createExtractor(self, listall = mycommands.ListAll) -> myutils.OutputExtractor:
        try:
            extractor = myutils.OutputExtractor(listall)
            return extractor
        except Exception as e:
            raise e
        
    def evaluate(self, extractor: myutils.OutputExtractor, answer: str):
        try:
            self.extractor = extractor
            self.outputStr = self.extractor.getOutput()
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(self.outputStr, answer)

    def unexpected(self, *args: Exception) -> print:
        print("There was a problem with testing the ListAll command.")
        myutils.Error(*args)
        raise

    def test_programsAndCommands(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, self.comboAnswer)

    def test_empty(self):
        try:
            testList = self.createListAll({}, {})
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, "")
    
    def test_onlyPrograms(self):
        try:
            testList = mycommands.ListAll(programDict = self.programDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, self.programAnswer)
    
    def test_onlyCommands(self):
        try:
            testList = mycommands.ListAll(commandDict = self.commandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, self.commandAnswer)

    def test_altDicts(self):
        testProgramDict = {"1": self.TestProgram()}
        testCommandDict = {"command": self.TestCommand(), "empty": None}
        testAnswer = "Available programs:\n 1: TestProgram\n\nAvailable commands:\n command\n empty\n"

        try:
            testList = self.createListAll(testProgramDict, testCommandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, testAnswer)

    def test_findProgram(self):
        try:
            testList = self.createListAll(self.programDict, {})
            program = testList.findProgram("BinaryMaskToDecimal")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(type(myprograms.BinaryMaskToDecimalProgram()), type(program))

    def test_findProgramNonexistent(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            program = testList.findProgram("meow")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(program, None)

    def test_findCommandByName(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            command = testList.findCommand("Clear")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(type(mycommands.ClearTerminal()), type(command))

    def test_findCommandByAlias(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            command = testList.findCommand("cls")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(type(mycommands.ClearTerminal()), type(command))

    def test_findCommandNonexistent(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            command = testList.findCommand("silly cat")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(command, None)

    def test_getHelpWithProgram(self):
        helpAnswer = myprograms.BinaryMaskToDecimalProgram.__doc__ + "\n"
        
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "BinaryMaskToDecimal")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)
        
    def test_getHelpWithCommandByName(self):
        helpAnswer = mycommands.ClearTerminal.__doc__ + "\n"
        
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "clear")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)

    def test_getHelpWithCommandByAlias(self):
        helpAnswer = mycommands.ClearTerminal.__doc__ + "\n"
        
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "cls")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)

    def test_getHelpWithHelp(self):
        helpAnswer = """Runs a program or command's inherited .help() method to print out the associated class's doc string. 

Type "help" followed by a command, program, or progam number to instantly print its help info. 
Ex: 
>>> help clear 
Clears the terminal. Works on posix and nt-like systems.\n"""
        
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "help")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)

    def test_getHelpWithQuit(self):
        helpAnswer = "Exits the terminal.\n"
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "quit")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)

    def test_getHelpNonexistent(self):
        helpAnswer = "Command or program not found.\n"
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
            outputStr = extractor.getOutput("getHelp", "silly cat")
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.assertEqual(outputStr, helpAnswer)

    def test_error_nonDict(self):
        answerStr = "ListAll only accepts dict objects."
        
        try:
            with self.assertRaises(TypeError) as e:
                self.createListAll(4, 5)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_CommandClassHasNoName(self):
        testProgramDict = {"1": self.TestProgram()}
        testCommandDict = {"command": self.TestCommandNameless(), "empty": None}
        testAnswer = "Command classes must have a name."

        try:
            with self.assertRaises(AttributeError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_error_ProgramClassHasNoName(self):
        testProgramDict = {"1": self.TestProgramNameless()}
        testCommandDict = {"command": self.TestCommand(), "empty": None}
        testAnswer = "Program classes must have a name."

        try:
            with self.assertRaises(AttributeError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_error_CommandNameNotStr(self):
        testProgramDict = {"1": self.TestProgram()}
        testCommandDict = {"command": self.TestCommandWeirdName(), "empty": None}
        testAnswer = "Command class name is not a string."

        try:
            with self.assertRaises(AssertionError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_error_ProgramNameNotStr(self):
        testProgramDict = {"1": self.TestProgramWeirdName()}
        testCommandDict = {"command": self.TestCommand(), "empty": None}
        testAnswer = "Program class name is not a string."

        try:
            with self.assertRaises(AssertionError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_error_CommandAliasNotList(self):
        testProgramDict = {"1": self.TestProgram()}
        testCommandDict = {"command": self.TestCommandWeirdAliases(), "empty": None}
        testAnswer = "Command aliases is not a list."

        try:
            with self.assertRaises(AssertionError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_error_CommandAliasNotString(self):
        testProgramDict = {"1": self.TestProgram()}
        testCommandDict = {"command": self.TestCommandWeirdAliasesString(), "empty": None}
        testAnswer = "Command alias is not a string."

        try:
            with self.assertRaises(AssertionError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)

    def test_eror_duplicateKey(self):
        testProgramDict = {"1": self.TestProgram(), "2": self.TestProgram}
        testCommandDict = {"command": self.TestCommand(), "empty": None}
        testAnswer = "Duplicate name or alias: \"testprogram\" already in dictionary."

        try:
            with self.assertRaises(ValueError) as e:
                self.createListAll(testProgramDict, testCommandDict)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, testAnswer)



if __name__ == '__main__':
    unittest.main()