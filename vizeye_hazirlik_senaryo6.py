ogrenci_sayisi = int(input("Öğrenci sayısını giriniz: "))
ogrenci_listesi = []

for i in range(ogrenci_sayisi):
    isim = input("Öğrenci adını giriniz: ")
    ogrenci_listesi.append(isim)

aranan_ogrenci = input("Kontrol etmek istediğiniz öğrencinin adını giriniz: ")
if aranan_ogrenci in ogrenci_listesi:
    print(aranan_ogrenci, "Sınıfta vardır.")
else:
    print(aranan_ogrenci, "Sınıfta yoktur.")

print("---Sınıf Yoklama Listesi---")
print(ogrenci_listesi)