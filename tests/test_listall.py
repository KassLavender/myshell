#!/opt/homebrew/bin/python3.13

import unittest

from context import mycommands, myprograms, myutils



class test_ListAll(unittest.TestCase):    
    programDict = {
            "1": myprograms.BinaryMaskToDecimalProgram()
        }
    commandDict = {
            "clear": mycommands.ClearTerminal()
        }
    programAnswer = "Available programs:\n 1: BinaryMaskToDecimal\n\n"
    commandAnswer = "Available commands:\n clear\n"
    comboAnswer = programAnswer + commandAnswer

    class TestProgram():
        name = "TestProgram"
    
    class TestCommand():
        name = "TestCommand"

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
        
    def eval(self, answer: str, extractor: myutils.OutputExtractor):
        try:
            self.extractor = extractor
            self.outputStr = self.extractor.getOutput()
        except Exception as e:
            raise e
        finally:
            self.assertEqual(self.outputStr, answer)

    def unexpected(self, *args: Exception) -> print:
        print("There was a problem with testing the listall command.")
        myutils.Error(*args)

    def test_programsAndCommands(self):
        try:
            testList = self.createListAll(self.programDict, self.commandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)
        
        if 'extractor' in locals():
            self.eval(self.comboAnswer, extractor)

    def test_empty(self):
        try:
            testList = self.createListAll({}, {})
            extractor = self.createExtractor(testList)
        except* Exception as e:
            myutils.Error(*e.exceptions)

        if 'extractor' in locals():
            self.eval("", extractor)
    
    def test_onlyPrograms(self):
        try:
            testList = self.createListAll(self.programDict, {})
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(self.programAnswer, extractor)
    
    def test_onlyCommands(self):
        try:
            testList = self.createListAll({}, self.commandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(self.commandAnswer, extractor)

    def test_altDicts(self):
        testProgramDict = {"test": self.TestProgram()}
        testCommandDict = {"test2": self.TestCommand()}
        testAnswer = "Available programs:\n test: TestProgram\n\nAvailable commands:\n TestCommand\n"
        try:
            testList = self.createListAll(testProgramDict, testCommandDict)
            extractor = self.createExtractor(testList)
        except* Exception as e:
            self.unexpected(*e.exceptions)

        if 'extractor' in locals():
            self.eval(testAnswer, extractor)

    def test_error_valueError(self):
        answerStr = "ListAll only accepts map objects."
        error = []
        
        try:
            self.createListAll(4, 5)
        except* Exception as e:
            error = [*e.exceptions]

        if len(error) == 1:
            self.assertEqual(str(error[0]), answerStr)
        else:
            self.unexpected(*error)



if __name__ == '__main__':
    unittest.main()