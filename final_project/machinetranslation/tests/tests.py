import unittest

from translator import frenchToEnglish, englishToFrench

class TestEnglish(unittest.TestCase):
    def testEn(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench(''),'')

class TestFrench(unittest.TestCase):
    def testFr(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(''),'')

unittest.main()