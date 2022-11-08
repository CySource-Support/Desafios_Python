import unittest

class isDivisibleTestCase(unittest.TestCase):
  
  def test_divisible(self):
    self.assertFalse(is_divisible(3,2,2))
    self.assertTrue(is_divisible(3,3,1))
    self.assertTrue(is_divisible(12,3,4))
    self.assertFalse(is_divisible(8,3,4))

def is_divisible(n, x, y):
    if (n % x) == 0 and  (n % y) == 0: 
        return True
    else:
        return False

unittest.main()