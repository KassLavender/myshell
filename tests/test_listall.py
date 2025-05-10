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
    
    class TestCommand():
        name = "TestCommand"

    class TestCommandWithAliases():
        name = "TestCommand2"
        aliases = ["secondtest"]

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
        print("There was a problem with testing the listall command.")
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
            testList = self.createListAll(self.programDict, {})
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        else:
            self.evaluate(extractor, self.programAnswer)
    
    def test_onlyCommands(self):
        try:
            testList = self.createListAll({}, self.commandDict)
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
        pass

    def test_findProgramNonexistent(self):
        pass

    def test_findCommand(self):
        pass

    def test_findProgramNonexistent(self):
        pass

    def test_getHelpWithProgram(self):
        pass

    def test_getHelpWithCommand(self):
        pass

    def test_getHelpWithHelp(self):
        pass

    def test_getHelpWithQuit(self):
        pass

    def test_getHelpNonexistent(self):
        pass

    def test_error_nonDict(self):
        answerStr = "ListAll only accepts dict objects."
        
        try:
            with self.assertRaises(ValueError) as e:
                self.createListAll(4, 5)
        except* Exception as f:
            self.unexpected(*f.exceptions)
        else:
            outputStr = str(e.exception)
            self.assertEqual(outputStr, answerStr)

    def test_error_CommandClassHasNoName(self):
        pass

    def test_error_ProgramClassHasNoName(self):
        pass

    def test_error_CommandNameNotStr(self):
        pass

    def test_error_ProgramNameNotStr(self):
        pass

    def test_error_ProgramAliasNotStr(self):
        pass

if __name__ == '__main__':
    unittest.main()