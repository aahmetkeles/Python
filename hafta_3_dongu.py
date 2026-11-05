#for bilet_no in range(1001,1006):
#    print("Bilet numarası:", bilet_no)


#sayac = 5
#while sayac > 0:
#    print("Sayaç:", sayac)
 #   sayac = sayac - 1
#print("Fırlatıldı!")


urun1 = int(input("Ürün 1i yazınız: "))
urun2 = int(input("Ürün 2i yazınız: "))
urun3 = int(input("Ürün 3ü yazınız: "))
toplam = sum([urun1, urun2, urun3])
if toplam > 50:
    print(f"Ürün fiyatı: {toplam * 90 / 100} TL'dir.")
else:
    print(f"Ürün fiyatı: {toplam} TL'dir.")

print("Toplam fiyat:", toplam)