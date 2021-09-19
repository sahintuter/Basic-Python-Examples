import time

saat, dakika, saniye = 0, 0, 0

while True:
    time.sleep(1)
    saniye += 1
    print(saat, ':', dakika, ':', saniye)

    if saniye == 60:
        saniye -= 60
        dakika += 1

    elif dakika == 60:
        saat += 1
