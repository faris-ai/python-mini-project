import random

def tebak(x):
    angka_random = random.randint(1,x)
    angka_tebakan = 0
    tebak_counter = 0
    while angka_tebakan != angka_random:
        while True:
            try:
                angka_tebakan = int(input(f"Tebak angka 1 - {x}: "))
                break
            except:
                print("Masukkan hanya angka!!")
        tebak_counter += 1

        selisih = 0
        if angka_tebakan < angka_random:
            selisih = angka_random - angka_tebakan
            if selisih < 4:
                print("Lebih tinggi sedikit (↑)")
            elif selisih < 11:
                print("Lebih tinggi (↑↑)")
            else:
                print("Lebih tinggi banget (↑↑↑)")
        elif angka_tebakan > angka_random:
            selisih = angka_tebakan - angka_random
            if selisih < 4:
                print("Lebih rendah sedikit (↓)")
            elif selisih < 11:
                print("Lebih rendah (↓↓)")
            else:
                print("Lebih rendah banget (↓↓↓)")

    print(f"\nSelamat Anda berhasil menebak angka {angka_random}")
    print(f"Anda menebak sebanyak {tebak_counter} kali")

is_main = True
while is_main:
    tebak(100)
    main_lagi = input("Main lagi? (y/n): ")
    if main_lagi == "n":
        is_main = False
    print("\n")
