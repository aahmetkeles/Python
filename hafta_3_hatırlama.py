#zaman dönüşümü
toplam_saniye = 197
dakika = toplam_saniye // 60
saniye = toplam_saniye % 60
print(f"{toplam_saniye} saniye = {dakika} dakika ve {saniye} saniye")

#mantıksal ve karşılaştırma operatörleri
yas = 20
bakiye = 450
bilet_fiyati = 350
yas_uygun = yas >=18
bakiye_yeterli = bakiye>=bilet_fiyati
satin_alinabilir = yas_uygun and bakiye_yeterli
print("Bilet satın alınabilir mi?: , satin_alinabilir")

#vücut kitle indeksi
kilo = 68
boy_metre = 1.75
vki = kilo / (boy_metre ** 2)
print("Vücut Kitle İndeksi:", round(vki, 1))

#hesap makinesi
sayi1 = 12
sayi2 = 4
print("\n--- Hesap Makinesi ---")
print("Toplama:", sayi1 + sayi2)
print("Çıkarma:", sayi1 - sayi2)
print("Çarpma:", sayi1 * sayi2)
print("Ondalıklı Bölme (/):", sayi1 / sayi2)
print("Tam Bölme (//):", sayi1 // sayi2)
print("Mod/Kalan (%):", sayi1 % sayi2)
print("Üs Alma (**):", sayi1 ** sayi2)