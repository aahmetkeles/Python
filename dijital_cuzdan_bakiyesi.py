# alıştırma 1
# mobil bankacılıktan bakiye metin geliyor sayısal göster
# bakiye_metni değişkenine "153.75" değerini (str olarak) atayın.
# float() kullanarak bunu bakiye adlı yeni bir değişkene dönüştürün.
# Dönüşümden önce ve sonra type() ile türleri karşılaştırın.

bakiye_metni = "153.75"
bakiye = float(bakiye_metni)
print(f"Dönüşümden önceki bakiye: {type(bakiye_metni)}")
print(f"Dönüşümden sonraki bakiye: {bakiye} TL - Tür: {type(bakiye)}")