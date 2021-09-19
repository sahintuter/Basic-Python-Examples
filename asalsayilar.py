from pyfiglet import Figlet

f = Figlet(font='standard')
print(f.renderText('Asal  Sayı  mı  ?'))

while True:

    sayi = int(input("Sayı giriniz:\n"))
    asal = True

    if sayi == 1:
        asal = False

    for i in range(2, sayi):
        if (sayi % i == 0):
            asal = False
        break
    if asal:
        print("Sayı asaldır\n")
    else:
        print("Asal değildir\n")
