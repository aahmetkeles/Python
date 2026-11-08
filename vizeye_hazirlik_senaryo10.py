kayitli_kullanici_adi = "ogrenci"
kayitli_sifre = "python2026"
deneme = 0
while deneme < 3:
    kullanici_adi = input("Lütfen kullanıcı adınızı yazınız:")
    sifre = input("Lütfen şifrenizi yazınız: ")
    if kullanici_adi == kayitli_kullanici_adi and sifre == kayitli_sifre:
        print("Giriş başarılı!")
        break
    else:
        deneme = deneme + 1
        kalan_hak = 3 - deneme
        if kalan_hak > 0:
            print("Giriş bilgileri hatalı, kalan deneme sayısı:", kalan_hak)
        else:
            print("3 defa üst üste hatalı giriş yaptınız. Hesabınız kilitlendi!")