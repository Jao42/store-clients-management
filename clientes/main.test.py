import unittest
from main import search

class testing(unittest.TestCase):
  def test_search(self):
    self.assertEqual(search('car', ['abobrinha', 'carlinhos', 'pedro']),
                     ['carlinhos'])
    self.assertEqual(search('o', ['abobrinha', 'carlinhos', 'pedro']),
                     ['abobrinha', 'carlinhos', 'pedro'])
    self.assertEqual(search('1', ['1', '2', '3012']),
                     ['1', '3012'])
    self.assertEqual(search(1, [1, 2, 3012]),
                     [1, 3012])


if __name__ == '__main__':
  unittest.main()





