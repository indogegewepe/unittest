import unittest
from geometry_calculator import GeometryCalculator

class GeometryCalculatorTest(unittest.TestCase):

    #arrage
    def setUp(self):
        self.alas = 5
        self.tinggi = 10

    def test_luas_segitiga(self):
        #act
        actualResult = GeometryCalculator.luas_segitiga(self.alas, self.tinggi)
        #assert
        expectedResult = 0.5 * self.alas * self.tinggi
        self.assertEqual(actualResult, expectedResult)

unittest.main()

