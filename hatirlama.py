# print sep end
print("=== İSTİNYE KAMPÜS KAFE ===")
print("Çay: 5 TL")
print("Kahve: 7 TL")
print("Tost: 10 TL")
print("Afiyet", end=" ")
print("olsun!\n")

#değişken
kullanici_adi ="Ahmet"
takipci = 1250
gizli_hesap = False
print("Profil:", kullanici_adi)
print("Takipçi:", takipci, "| Gizli mi?", gizli_hesap)

#değişken değiştirme
sarj =20
print("İlk Şarj:", sarj)
sarj = sarj + 10
print("Güncellenmiş Şarj:", sarj)

#tür sorgulama
isim = "Ahmet"
yas = 24
boy = 1.82
prim_uye = True

print(type(isim), type(yas), type(boy), type(prim_uye))

#tip dönüşümü
bakiye_metni = "153.75"
bakiye = float(bakiye_metni)
print("Dönüştürülen Bakiye:", bakiye, "| Türü:", type(bakiye))

#yaş sınırı hesaplama
dogum_yili_metni = "2007"
dogum_yili = int(dogum_yili_metni)
hesaplanan_yas = 2026 - dogum_yili
icerik_izni = hesaplanan_yas >= 18
print(f"Yaş: {hesaplanan_yas} | 18+ İzni Var Mı?: {icerik_izni}")

# ondalıklı metni tam sayıya yuvarlayarak çevirme
boy_metni = "184.6"
boy_yuvarlanmis = round(float(boy_metni))
print("Yuvarlanmış Boy:", boy_yuvarlanmis)