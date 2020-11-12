import unittest
import test

class testiranje(unittest.TestCase):
    def test_prvitest(self):
        a= test.mul(4,5)
        self.assertEqual(a,21)

if __name__=="__main__":
    unittest.main()
