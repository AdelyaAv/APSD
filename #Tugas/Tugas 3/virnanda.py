print("PROGRAM HITUNG NILAI AKHIR")

# Input data siswa
nama_siswa = input("Nama Siswa : ")
nilai_keaktifan = float(input("Nilai Keaktifan : "))
nilai_tugas = float(input("Nilai Tugas : "))
nilai_ujian = float(input("Nilai Ujian : "))

# Proses perhitungan nilai murni
nilai_murni_keaktifan = nilai_keaktifan * 0.20
nilai_murni_tugas = nilai_tugas * 0.30
nilai_murni_ujian = nilai_ujian * 0.50

# Hitung nilai akhir
nilai_akhir = nilai_murni_keaktifan + nilai_murni_tugas + nilai_murni_ujian

# Tentukan grade
if nilai_akhir > 80:
    grade = "A"
elif nilai_akhir > 70:
    grade = "B"
elif nilai_akhir > 56:
    grade = "C"
elif nilai_akhir > 46:
    grade = "D"
else:
    grade = "E"

# Output hasil
print("\nLayar Keluaran")
print("Siswa yang bernama", nama_siswa)
print("Dengan Nilai Persentasi Yang dihasilkan:")
print("Nilai Keaktifan * 20% :", nilai_murni_keaktifan)
print("Nilai Tugas * 30% :", nilai_murni_tugas)
print("Nilai Ujian * 50% :", nilai_murni_ujian)
print("Jadi Siswa yang bernama", nama_siswa, "memperoleh nilai akhir sebesar", nilai_akhir, "dengan grade", grade)