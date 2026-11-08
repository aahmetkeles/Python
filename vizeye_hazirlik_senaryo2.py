urun1 = input("Lütfen 1. ürünün adını giriniz: ")
fiyat1 = float(input("Lütfen 1. ürünün fiyatını giriniz: "))

urun2 = input("Lütfen 2. ürünün adını giriniz: ")
fiyat2 = float(input("Lütfen 2. ürünün fiyatını giriniz: "))

urun3 = input("Lütfen 3. ürünün adını giriniz: ")
fiyat3 = float(input("Lütfen 3. ürünün fiyatını giriniz: "))

urunler = [urun1, urun2, urun3]
fiyatlar = [fiyat1, fiyat2, fiyat3]

toplam = 0
for fiyat in fiyatlar:
    toplam = toplam + fiyat

if toplam >= 1000:
    indirimli_toplam = toplam * 0.90
elif toplam >= 500:
    indirimli_toplam = toplam * 0.95
else:
    indirimli_toplam = toplam

print("--- Alışveriş Özeti ---")
print("Alınan ürünler:", urunler)
print("İndirimsiz Toplam:", toplam)
print("Ödenecek Toplam Fiyat:", indirimli_toplam)