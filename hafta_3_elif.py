puan = int(input("Puanınızı girin: "))
if puan >= 1000:
    print("Altın seviye")
elif puan >= 500:
    print("Gümüş seviye")
elif puan >= 300:
    print("Bronz seviye")
else:
    print("Seviye belirlenemedi.")