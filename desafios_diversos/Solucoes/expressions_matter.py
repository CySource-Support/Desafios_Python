# Solução do desafio Expression Matter by Jonas

import unittest

class matterTestCase(unittest.TestCase):

  def test_basic_expression_matter(self):
    test = [[2, 1, 2], [2, 1, 1], [2, 2, 4], [3, 3, 3], \
            [1, 1, 1], [1, 2, 3], [1, 3, 1], [2, 2, 2], \
            [5, 1, 3], [3, 5, 7], [5, 6, 1], [1, 6, 1], \
            [2, 6, 1], [6, 7, 1], [2, 10, 3], [1, 8, 3],\
            [9, 7, 2], [1, 1, 10], [9, 1, 1], [10, 5, 6],\
            [1, 10, 1]]
    result = [6, 4, 16, 27, 3, 9, 5, 8, 20, 105, 35, \
              8, 14, 48, 60, 27, 126, 20, 18, 300, 12]
    for i in range(len(test)):
      self.assertEquals(expression_matter(*test[i]), result[i])


def expression_matter(a, b, c):
  # Aqui vai seu código
  return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))  # aqui vai a resposta

unittest.main()
