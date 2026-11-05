deneme = 0
dogru_sifre = "ist2026"
while deneme < 3:
    sifre = input("Şifreyi giriniz: ")
    if sifre == dogru_sifre:
        print("Giriş başarılı!")
        break
    else:
        deneme += 1
        print(f"Hatalı şifre! Kalan deneme hakkınız: {3 - deneme}")