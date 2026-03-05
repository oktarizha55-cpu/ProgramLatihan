

# 1.Split bill nongkrong 
tagihan = float (input ("Masukin total tagihan nya"))
orang = int (input ("Masukin jumlah orang nya"))

pajak = 0.10 * tagihan
total = tagihan + pajak
per_orang = total / orang 
print ("Total tagihan: " + str(total))

print ("Total setelah bayar pajak : ", total)
print ("Bayar per orang : ", per_orang)

# 2. Konversi Waktu Kerja Freelance
jam = float (input ("Masukan jumlah jam kerja freelance: "))
menit = float (input ("Masukan menit kerja freelance: "))
upah_per_jam = float (input ("Masukan Upah per jam nya : "))

total_jam = jam + (menit / 60)
bayaran = total_jam * upah_per_jam

print ("Total jam kerja freelance: " + str(total_jam))

#3. Tabungan Target Laptop

harga_laptop = float (input ("Masukan harga laptop yang ingin dibeli: "))
tabungan_per_bulan = float (input ("Masukan jumlah tabungan per bulan: "))

bulan = harga_laptop / tabungan_per_bulan

print ("Jumlah bulan yang dibutuhkan untuk mencapai target tabungan: " + str(bulan))

#4. Estimasi biaya BBM untuk perjalanan 
jarak = float (input ("Masukan jarak tempuh perjalanan dalam kilometer: "))
harga = 13000
liter = 12
biaya_bbm = (jarak / liter) * harga

print ("Liter bensin : ", liter)
print ("Total biaya BBM untuk perjalanan: " + str(biaya_bbm))

#5. Gaji net Karyawan 
gaji_pokok = float (input ("Masukan gaji kotor bulanan: "))
tunjangan = 750000

gaji_kotor = gaji_pokok + tunjangan

bpjs = 0.02 * gaji_kotor
pajak = 0.05 * gaji_kotor

gaji_bersih = gaji_kotor - bpjs - pajak
print ("Gaji bersih:", gaji_bersih)

#6. Luas cat dinding rumah 

p = float (input ("Panjang kamar: "))
l =float (input ("Lebar kamar: "))
t = float (input ("Tinggi kamar: "))

luas = 2* (p*t) + 2*(l*t)
kaleng = luas / 10 

print ("Luas dinding yang akan dicat: " + str(luas))
print ("Jumlah kaleng cat yang dibutuhkan: " + str(kaleng))

#7. konsumsi air harian keluarga 
orang = int (input ("Masukan jumlah anggota keluarga: "))

air_hari = orang * 150
air_minggu = air_hari * 7

galon = air_minggu / 19
biaya = galon *19000

print ("Air per minggu: " + str(air_minggu) + " liter")
print ("Jumlah galon yang dibutuhkan per minggu: " + str(galon))
print ("Total biaya air per minggu: " + str(biaya))

#8. penyusutan nilai laptop 
harga_awal = 12000000
nilai_sisa = 2000000
umur = 4 

penyusutan = (harga_awal - nilai_sisa) / umur
nilai_2_tahun = harga_awal - (penyusutan * 2)

print ("Penyusutan per tahun: " + str(penyusutan))
print ("Nilai laptop setelah 2 tahun: " + str(nilai_2_tahun))
