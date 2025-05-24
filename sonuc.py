
def sadece_sayi_gir(mesaj):
    while True:
        veri = input(mesaj)
        if veri.isdigit():
            return int(veri)
        else:
            print("Lütfen sadece sayı girin.")

def durum():
    v1 = sadece_sayi_gir("1. vize notunuz kaçtır: ")
    v2 = sadece_sayi_gir("2. vize notunuz kaçtır: ")
    finl = sadece_sayi_gir("Final notunuz kaçtır: ")

    ort = (v1 * 0.2) + (v2 * 0.2) + (finl * 0.6)

    print(f"Ortalamanız: {ort:.2f}")

    if ort >= 60 and finl >= 50:
        print("Tebrikler, sınavdan geçtiniz.")
    else:
        print("Üzgünüz, sınavdan kaldınız.")

durum()

