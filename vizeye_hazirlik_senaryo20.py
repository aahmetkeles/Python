adimlar = []

for i in range(1,8):
    gunluk_adim = int(input("Adım sayısını giriniz: "))
    adimlar.append(gunluk_adim)

hedefe_ulasilan_gun = 0
for adim in adimlar:
    if adim >= 8000:
        hedefe_ulasilan_gun = hedefe_ulasilan_gun + 1

toplam_adim = sum(adimlar)
ortalama_adim = toplam_adim / len(adimlar)

print("---Haftalık Adım Listesi---")
print("Adım listesi:", adimlar)
print("Toplam adım sayısı:", toplam_adim)
print("Ortalama adım sayısı:", ortalama_adim)
print("Hedefe ulaşılan gün sayısı:", hedefe_ulasilan_gun)