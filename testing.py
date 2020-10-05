import unittest
from more_functions import FunctionParam as Function

class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(Function.multiply_string("Ayah",3),Function.multiply_string("Ayah",3))
        print(Function.multiply_string("Ayah",3))


if __name__ == '__main__':
    unittest.main()
