import random
import string
def sifre_uret(uzunluk):
    harf =  string.ascii_letters + string.digits + string.punctuation
    sonuc = ''.join(random.choice(harf) for i in range(uzunluk))
    return sonuc
try:
    karakter_sayı = int(input("Şifre kaç karakter olsun : "))
    print("1. Örnek şifre : " + sifre_uret(karakter_sayı))
    print("2. Örnek şifre : " + sifre_uret(karakter_sayı))
    print("3. Örnek şifre : " + sifre_uret(karakter_sayı))
except ValueError:
    print("Lütfen sadece sayı girin!")

