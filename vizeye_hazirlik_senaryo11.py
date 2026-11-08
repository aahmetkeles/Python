ogrenci_sayisi = int(input("Öğrenci sayısını giriniz: "))
notlar = []

for i in range(ogrenci_sayisi):
    not_degeri = int(input("Öğrencinin notunu giriniz: "))
    notlar.append(not_degeri)

toplam_not = sum(notlar)
ortalama = toplam_not / len(notlar)

en_yuksek = max(notlar)
en_dusuk = min(notlar)

print("---Sınav Notları---")
print("Not listesi:", notlar)
print("Ortalama:", ortalama)
print("En yüksek puan:", en_yuksek)
print("En düşük puan:", en_dusuk)