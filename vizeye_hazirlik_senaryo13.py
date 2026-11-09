olcum_listesi = []

for i in range(5):
    olcum= float(input("Lütfen ölçümü giriniz: "))
    olcum_listesi.append(olcum)

print("---Sıcaklık Ölçüm Listesi---")

for olcum in olcum_listesi:
    if olcum < 0:
        print(olcum, "derece: Sıcaklık düşük")
    elif olcum <= 30:
        print(olcum, "derece: Sıcaklık normal")
    else:
        print(olcum, "derece: Sıcaklık yüksek")