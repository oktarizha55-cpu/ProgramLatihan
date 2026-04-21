# 1. Hitung banyak angka kelipatan 3 dari 1–100
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Jumlah kelipatan 3 dari 1-100:", count)

print("\n------------------------\n")

# 2. Menjumlahkan input user (5 kali)
total = 0
for i in range(5):
    angka = int(input("Masukkan angka ke-" + str(i+1) + ": "))
    total += angka
print("Total jumlah:", total)

print("\n------------------------\n")

# 3. Validasi input angka positif
angka = int(input("Masukkan angka positif: "))
while angka < 0:
    print("Angka harus positif!")
    angka = int(input("Masukkan lagi: "))
print("Angka yang benar:", angka)

print("\n------------------------\n")

# 4. Rata-rata nilai (5 input)
total_nilai = 0
for i in range(5):
    nilai = int(input("Masukkan nilai ke-" + str(i+1) + ": "))
    total_nilai += nilai

rata = total_nilai / 5
print("Rata-rata nilai:", rata)

print("\n------------------------\n")

# 5. Menu sederhana (while loop)
while True:
    print("\nMenu:")
    print("1. Halo")
    print("2. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("Halo User")
    elif pilih == "2":
        print("Program berhenti")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
