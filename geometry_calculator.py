class GeometryCalculator:
    def luas_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi
    def luas_persegi_panjang(panjang, lebar):
        return panjang * lebar
    def luas_jajargenjang(alas, tinggi):
        return alas * tinggi
    def luas_persegi(sisi):
        return sisi * sisi

print(GeometryCalculator.luas_segitiga(10, 5))
print(GeometryCalculator.luas_persegi_panjang(10, 5))
print(GeometryCalculator.luas_jajargenjang(10, 5))
print(GeometryCalculator.luas_persegi(10))