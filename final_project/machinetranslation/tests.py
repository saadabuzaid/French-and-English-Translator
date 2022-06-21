'''
A unit test to test the functions and null inputted
There is a current problem with managing modules in
standard python packages; as a result, this module is not in test package
'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''
    A class to test English to french translations using assertions
    '''
    def test_english_to_french(self):
        '''
        A function to test translation of the english_to_french function
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

    def test_null_input_en_fr(self):
        '''
        A function that tests the null input in the english_to_french function
        '''
        self.assertIsNone(english_to_french(None))

class TestFrenchToEnglish(unittest.TestCase):
    '''
    A class to test French to English translations using assertions
    '''
    def test_french_to_english(self):
        '''
        A function to test translation of the french_to_english function
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")

    def test_french_to_english_null_input(self):
        '''
        A function that tests the null input in the french_to_english function
        '''
        self.assertIsNone(french_to_english(None))

unittest.main()
