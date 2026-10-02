# alıştırma 3
dogum_yili_metni = "2007"
dogum_yili = int(dogum_yili_metni)
yas = 2026 - dogum_yili
icerik_izni_var_mi = yas >= 18
print(f"Yaş: {yas} (Türü: {type(yas)})")
print(f"İçerik izni var mı?: {icerik_izni_var_mi} (Türü: {type(icerik_izni_var_mi)})")