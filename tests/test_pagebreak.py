#!/opt/homebrew/bin/python3.13

import unittest

from context import mycommands, myutils



class test_PageBreak(unittest.TestCase):
    """Tests the pagebreak command."""

    def test_PageBreak(self):
        dataStr = "—————————————————————————————\n"

        try:
            testPageBreak = myutils.OutputExtractor(mycommands.PageBreak())
            answerStr = testPageBreak.getOutput()
        except* Exception as e:
            myutils.Error(*e.exceptions)
        else:
            self.assertEqual(dataStr, answerStr)



if __name__ == '__main__':
    unittest.main()