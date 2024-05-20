# Menerima input dari pengguna
nama_karyawan = input("Nama Karyawan: ")
golongan_jabatan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jumlah_jam_kerja = float(input("Jumlah jam kerja: "))

# Gaji pokok
gaji_pokok = 300000

# Tunjangan Jabatan
if golongan_jabatan == 1:
    tunjangan_jabatan = gaji_pokok * 0.05
elif golongan_jabatan == 2:
    tunjangan_jabatan = gaji_pokok * 0.1
elif golongan_jabatan == 3:
    tunjangan_jabatan = gaji_pokok * 0.15
else:
    tunjangan_jabatan = 0

# Tunjangan Pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = gaji_pokok * 0.025
elif pendidikan == "D1":
    tunjangan_pendidikan = gaji_pokok * 0.05
elif pendidikan == "D3":
    tunjangan_pendidikan = gaji_pokok * 0.2
elif pendidikan == "S1":
    tunjangan_pendidikan = gaji_pokok * 0.3
else:
    tunjangan_pendidikan = 0

# Honor Lembur
jam_lembur = max(jumlah_jam_kerja - 8, 0)
honor_lembur = jam_lembur * 3500

# Gaji total
gaji_total = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Menampilkan hasil
print(f"Karyawan yang bernama {nama_karyawan}")
print("\nHonor yang diterima:")
print(f"Tunjangan Jabatan: Rp {tunjangan_jabatan:.2f}")
print(f"Tunjangan Pendidikan: Rp {tunjangan_pendidikan:.2f}")
print(f"Honor Lembur: Rp {honor_lembur:.2f}")
print(f"\nTotal Gaji: Rp {gaji_total:.2f}")
