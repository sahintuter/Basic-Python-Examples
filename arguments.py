"""
# --girilen kelimeyi belirtilen sayı kadar yazan fonksiyon--

klm = input("kelime giriniz:")
say = int(input("sayı giriniz:"))


 def yaz(kelime, sayi):
   print(klm*say)


yaz(klm, say)

 ----------------------------------------

 --Gönderilen parametreleri listeye ekleyen fonksiyon--


 def ekle(*prmtre):
   liste = []
    for pr in prmtre:
        liste.append(pr)
    return liste
girinti = ekle(1, 2, 3, 4, 5, "python")
 print(girinti)
 ----------------------------------------------

--girilen iki sayı arasındaki asal sayıları bulan fonksiyon--


def asal(sayi1, sayi2):
    for i in range(sayi1, sayi2+1):
        if i > 1:
            for s in range(2, i):
                if (i % s == 0):
                    break
            else:
                print(i)


sayi1 = int(input("İlk sayıyı giriniz:\n"))
sayi2 = int(input("İkinci sayıyı giriniz\n"))

asal(sayi1, sayi2)
------------------------------

# Girilen sayının tam bölenlerini listeye ekleyen fonksiyon


def tam(sayi):
    liste = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            liste.append(i)
    return liste


print(tam(20))
---------------------------------


# Fonsiyonlarda "map methodu"


def sayilar(say):
    return say**2


rakam = [1, 2, 3, 4]


res = list(map(sayilar, rakam))

#for item in map(sayilar, rakam):   "for dögüsü ile çalıştıra yöntemi"
# print(item)

print(res)
#---------------------------
# lambda kullanımı

rakam = [1, 2, 3, 4]

res = list(map(lambda say: say ** 2, rakam))
# fonksiyon tanımlamadan lambda ile aynı işlem yapılabilir

print(res)
"""
