class GeometryCalculator:

    def luas_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi
    def luas_persegi_panjang(panjang, lebar):
        return panjang * lebar
    def luas_jajargenjang(alas, tinggi):
        return alas * tinggi
    def luas_persegi(sisi):
        return sisi * sisi
    
    def diameter_lingkaran(self, jarijari):
        return 2 * jarijari
    def luas_lingkaran(self, jarijari):
        diameter = self.diameter_lingkaran(jarijari)
        return (1/4) * 3.14159265359 * (diameter * diameter)