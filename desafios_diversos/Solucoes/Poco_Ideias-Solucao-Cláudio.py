import unittest

class wellTestCase(unittest.TestCase):
  def test_well_fail(self):
    self.assertEqual(well(['bad', 'bad', 'bad']), 'Falha!')
  
  def test_well_publish(self):
    self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publicar!')

  def test_well_series(self):
    self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'Sinto cheiro de série!')

def well(array):
    if array.count("good") > 2:
        return 'Sinto cheiro de série!'
    elif array.count("good") == 1:
        return 'Publicar!'
    else:
        return 'Falha!'
unittest.main()