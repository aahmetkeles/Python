# alıştırma 4 ilk 2 haftadaki herşeyin kapsamlı alıştırması
# oyuncunun hesap bilgileri metin formatında bunları gerekli formatlara çevir ve profil kartı yap

oyuncu_adi = "ShadowWalker"
bakiye_metni = "450.85"        # str
oyun_fiyati_metni = "120.40"   # str
seviye_metni = "24"            # str
premium_uye_mi = True          # bool

bakiye = float(bakiye_metni)
oyun_fiyati = float(oyun_fiyati_metni)
seviye = int(seviye_metni)
kalan_bakiye = bakiye - oyun_fiyati
seviye = seviye + 1 # oyunu aldığı için seviyesi arttı
yuvarlanan_bakiye = round(kalan_bakiye)
usta_oyuncu_mu = seviye >= 25

print("\n--- OYUNCU HESAP ÖZETİ ---")
print(f"Oyuncu: {oyuncu_adi} -- Premium: {premium_uye_mi}")
print(f"Yeni Seviye: {seviye} (Türü: {type(seviye)})")
print(f"Usta Oyuncu Statüsü: {usta_oyuncu_mu}")

print("\n--- HARCAMA DETAYI ---")
print(f"Eski Bakiye: {bakiye} TL")
print(f"Oyun Fiyatı: {oyun_fiyati} TL")
print(f"Kalan Bakiye: {kalan_bakiye:.2f} TL (Yaklaşık: {yuvarlanan_bakiye} TL)") 
# kalan bakiyenin yanına :.2f koyunca kalan bakiyeyi daha düzgün gösterdi
# yoksa çok fazla sıfırı yan yana sıralıyordu gereksiz yere
print(f"Kalan Bakiye Veri Türü: {type(kalan_bakiye)}")