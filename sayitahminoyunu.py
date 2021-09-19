import random
from pyfiglet import Figlet

f = Figlet(font='standard')
print(f.renderText('sayı tahmin'))

sayi = random.randint(1, 10)

canSayisi = int(input("Kaç hak kullanmak istersiniz:\n"))
hak = canSayisi
sayac = 0

while hak > 0:
    sayac += 1
    hak -= 1

    tahmin = int(input("Tahmininiz:\n"))

    if sayi == tahmin:
        print(
            f"Tebrikler, {sayac}. tahmininizde bildiniz. Puanınız {100-(100/canSayisi)*(sayac-1)}")
        break
    elif sayi < tahmin:
        print("Daha küçük bir sayı giriniz\n")
    else:
        print("Daha büyük bir sayı giriniz\n")
    if hak == 0:
        print(f"Tahmin hakkınız bitti :( Tutulan sayı : {sayi}\n")
