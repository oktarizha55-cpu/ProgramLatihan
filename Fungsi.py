# =========================================================
# SOAL 1: Kalkulator Patungan Makan Malam (Split Bill)
# =========================================================
def hitung_patungan(total_nota, jumlah_orang, persen_tips):
    total_dengan_tips = total_nota + (total_nota * persen_tips / 100)
    bayar_per_orang = total_dengan_tips / jumlah_orang
    return bayar_per_orang


# =========================================================
# SOAL 2: Sistem Gaji Lembur Karyawan
# =========================================================
def hitunggajilembur(gaji_pokok, totaljamkerja):
    if totaljamkerja > 40:
        jam_lembur = totaljamkerja - 40
        upah_lembur = jam_lembur * 50000
        total_gaji = gaji_pokok + upah_lembur
    else:
        total_gaji = gaji_pokok
    return total_gaji


# =========================================================
# SOAL 3: Format Alamat Pengiriman E-Commerce
# =========================================================
def format_alamat(jalan, kota, provinsi, kode_pos):
    alamat = f"Jalan: {jalan}, Kota: {kota}, {provinsi} ({kode_pos})"
    return alamat


# =========================================================
# SOAL 4: Konversi Waktu Menonton Beruntun (Binge-Watching)
# =========================================================
def konversi_menit(jumlah_episode, durasiperepisode):
    total_menit = jumlah_episode * durasiperepisode
    jam = total_menit // 60
    menit_sisa = total_menit % 60
    return jam, menit_sisa


# =========================================================
# SOAL 5: Validasi Kupon Diskon Bioskop
# =========================================================
def cek_diskon(total_harga, jumlah_tiket, kode_kupon):
    if kode_kupon == "NONTONSERU" and jumlah_tiket >= 2:
        total_harga = total_harga - 15000
    return total_harga


# =========================================================
# SOAL 6: Filter Nilai Kelulusan Siswa (Boolean Return)
# =========================================================
def apakah_lulus(nilai_siswa, nilai_kkm):
    return nilai_siswa >= nilai_kkm


# =========================================================
# SOAL 7: Generator Username Akun Baru
# =========================================================
def buat_username(nama_lengkap, tahun_lahir):
    kata_pertama = nama_lengkap.split()[0].lower()
    dua_digit_tahun = str(tahun_lahir)[-2:]
    username = kata_pertama + dua_digit_tahun
    return username


# =========================================================
# SOAL 8: Estimasi Waktu Tiba (ETA) Ojek Online
# =========================================================
def estimasi_tiba(jarak_km, kondisi_cuaca):
    total_waktu = jarak_km * 3
    if kondisi_cuaca == "hujan":
        total_waktu += 10
    return total_waktu


# =========================================================
# SOAL 9: Fitur Pembatasan Karakter Tweet (Sosial Media)
# =========================================================
def validasi_tweet(teks_input):
    if len(teks_input) <= 140:
        return teks_input
    else:
        return teks_input[:140] + "..."


# =========================================================
# SOAL 10: Sistem Poin Loyalitas Toko (Multiple Return Condition)
# =========================================================
def hitungpoinbelanja(total_transaksi, status_member):
    if status_member == False:
        return 0
    poin = total_transaksi // 20000
    return poin


# =========================================================
# CONTOH PENGUJIAN (TESTING) SEMUA FUNGSI
# =========================================================
if __name__ == "__main__":
    print("Soal 1:", hitung_patungan(300000, 4, 10))
    print("Soal 2:", hitunggajilembur(2000000, 45))
    print("Soal 3:", format_alamat("Jl. Mawar No. 1", "Bandung", "Jawa Barat", "40123"))
    print("Soal 4:", konversi_menit(5, 45))
    print("Soal 5:", cek_diskon(100000, 2, "NONTONSERU"))
    print("Soal 6:", apakah_lulus(75, 70))
    print("Soal 7:", buat_username("Budi Santoso", 1998))
    print("Soal 8 (cerah):", estimasi_tiba(10, "cerah"))
    print("Soal 8 (hujan):", estimasi_tiba(10, "hujan"))
    print("Soal 9:", validasi_tweet("Halo dunia!"))
    print("Soal 10 (member):", hitungpoinbelanja(95000, True))
    print("Soal 10 (bukan member):", hitungpoinbelanja(95000, False))