#askeri liseye girme durumu
yas = int(input("Yaşınızı giriniz: "))
if yas >= 18:
    print("Yaş şartı sağlandı.")
    boy = int(input("Boyunuzu giriniz: "))
    if boy >= 170:
        print("Askeri liseye girebilirsiniz!")
    else:
        print("Boy şartı sağlanamadı. Askeri liseye giremezsiniz.")
else:
    print("Yaş şartı sağlanamadı. Askeri liseye giremezsiniz.")