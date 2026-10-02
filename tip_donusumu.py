# int sayıya çevirir
# float ondalık sayıya çevirir
# str metne çevirir
# bool mantıksal değere çevirir

# Web formundan gelen veri örneği
yas_metni = "20"
# print(yas_metni + 5)  --> HATA VERİR! (str ile int toplanamaz)

yas_sayi = int(yas_metni)
print(f"5 yıl sonraki yaş: {yas_sayi + 5}")  # Çıktı: 25

#int ondalığı yuvarlamaz sadece tam kısmı alır
boy = 181.8
print(int(boy)) # Çıktı: 181
# round ise yuvarlar
print(round(boy)) # Çıktı: 182

# ondalıklı sayı metin ise önce float sonra int
tam_sayi = round(float(boy))
print(f"Sonuç: {tam_sayi}") # Çıktı: 182