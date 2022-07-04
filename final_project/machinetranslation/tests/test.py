import unittest
from translator import englishToFrench, frenchToEnglish # pylint: disable=import-error


class TestTranslator(unittest.TestCase):
    '''
    Test 1
'''

    def test_englishtofrench(self):
        '''
        Test Equal
    '''
        self.assertEqual(englishToFrench("Hello"),'Bonjour')

class TestTranslator2(unittest.TestCase):
    '''
    Test 1
'''

    def test_englishtofrench(self):
        '''
        Test Not Equal
        '''
        self.assertNotEqual(englishToFrench("Hello"), "Hello")


class TestTranslator3(unittest.TestCase):
    '''
    Test 1
    '''
    def test_englishtofrench(self):
        '''
        Test Equal
        '''
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")



class TestTranslator4(unittest.TestCase):
    '''
    Test 1
    '''

    def test_englishtofrench(self):
        '''
        Test Not Equal
        '''
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
