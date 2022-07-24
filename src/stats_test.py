import unittest

from stats import fav_languages

class TestFavLanguages(unittest.TestCase):
    def test_empty(self):
        testcase = {'repos':[]}
        expected = []
        self.assertEqual(fav_languages(testcase),expected)

    def test_one_lang(self):
        testcase = {'repos':[{'name': "Test1", 'owner': "Olga", 'language': "Python"}]}
        expected = [{'freq': 1, 'name': 'Python'}]
        self.assertEqual(fav_languages(testcase),expected)
        
    def test_many_langs(self):
        testcase = {'repos':[{'name': "Test1", 'owner': "Olga", 'language': "Python"}, 
        {'name': "Test2", 'owner': "Olga", 'language': "Html"},
        {'name': "Test3", 'owner': "Olga", 'language': "CSS"},
        {'name': "Test4", 'owner': "Olga", 'language': "Python"},
        {'name': "Test5", 'owner': "Olga", 'language': "JavaScript"},
        {'name': "Test6", 'owner': "Olga", 'language': "C++"},
        {'name': "Test7", 'owner': "Olga", 'language': "Html"},
        {'name': "Test8", 'owner': "Olga", 'language': "Python"},
        {'name': "Test9", 'owner': "Olga", 'language': "Html"},
        {'name': "Test10", 'owner': "Olga", 'language': "Python"},
        {'name': "Test11", 'owner': "Olga", 'language': "CSS"}]}
        expected = [{'freq': 4, 'name': 'Python'}, {'freq': 3, 'name': 'Html'}, {'freq': 2, 'name': 'CSS'}]
        self.assertEqual(fav_languages(testcase),expected)

if __name__ == "__main__":
    unittest.main()