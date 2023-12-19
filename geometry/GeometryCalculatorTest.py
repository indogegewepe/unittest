import unittest
from geometry_calculator import GeometryCalculator

class GeometryCalculatorTest(unittest.TestCase):

    #arrage
    def setUp(self):
        self.alas = 5
        self.tinggi = 10
        self.panjang = 5
        self.lebar = 10
        self.sisi = 5
        self.jarijari = 10

    def test_luas_segitiga(self):
        #act
        actualResult = GeometryCalculator.luas_segitiga(self.alas, self.tinggi)
        #assert
        expectedResult = 0.5 * self.alas * self.tinggi
        self.assertEqual(actualResult, expectedResult)

    def test_luas_persegi_panjang(self):
        #act
        actualResult = GeometryCalculator.luas_persegi_panjang(self.panjang, self.lebar)
        #assert
        expectedResult = self.panjang * self.lebar
        self.assertEqual(actualResult, expectedResult)

    def test_luas_jajargenjang(self):
        #act
        actualResult = GeometryCalculator.luas_jajargenjang(self.alas, self.tinggi)
        #assert
        expectedResult = self.alas * self.tinggi
        self.assertEqual(actualResult, expectedResult)

    def test_luas_persegi(self):
        #act
        actualResult = GeometryCalculator.luas_persegi(self.sisi)
        #assert
        expectedResult = self.sisi * self.sisi
        self.assertEqual(actualResult, expectedResult)
    
    def test_luas_lingkaran(self):
        #act
        geometryCalculator = GeometryCalculator()
        actualResult = geometryCalculator.luas_lingkaran(self.jarijari)
        #assert
        diameter = geometryCalculator.diameter_lingkaran(self.jarijari)
        expectedResult = (1/4) * 3.14159265359 * (diameter * diameter)
        self.assertEqual(actualResult, expectedResult)

unittest.main()