import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(validate.test_score("Chem",0),validate.test_score("Chem",0))
    def test_below(self):
        self.assertEqual(validate.test_score("Chem",-1),validate.test_score("Chem",-1))
    def test_above(self):
        self.assertEqual(validate.test_score("Chem", 104), validate.test_score("Chem", 104))
    def test_invalid_message(self):
        self.assertEqual(validate.test_score("Chem",98, "Bad Input"),validate.test_score("Chem",98, "Bad Input"))




if __name__ == '__main__':
    unittest.main()
