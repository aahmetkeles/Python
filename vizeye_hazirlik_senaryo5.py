bakiye = 5000.0
devam = "evet"
while devam == "evet":
    tutar = float(input("Lütfen çekmek istediğiniz tutarı giriniz: "))
    if tutar <= 0:
        print("Lütfen 0'dan büyük bir sayı giriniz.")
    elif tutar > bakiye:
        print("Yetersiz bakiye!")
    else:
        bakiye = bakiye - tutar
        print("İşlem başarılı, kalan bakiyeniz:", bakiye)
    devam = input("Devam etmek istiyor musunuz? (evet/hayır): ")
print("Program sonlandırıldı.")