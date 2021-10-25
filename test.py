import unittest

class Test(unittest.TestCase):
    def test(self):
        a=15
        self.assertEqual(a,15)
    # def test_add(self):
    #     self.assertEqual(cal.add(10,10),20)
    #     self.assertEqual(cal.add(10,1),11)

if __name__=='__main__':
    unittest.main()