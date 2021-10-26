import unittest
import sample

class TestArithmetic (unittest.TestCase):

    def test_square(self):
        num = 4
        result = sample.take_square(num)
        self.assertEqual(result, 25)
if __name__ == '__main__':
    unittest.main()