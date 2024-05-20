print("PROGRAM HITUNG NILAI AKHIR")

# Input data siswa
nama_siswa = input("Nama Siswa : ")
nilai_keaktifan = float(input("Nilai Keaktifan : "))
nilai_tugas = float(input("Nilai Tugas : "))
nilai_ujian = float(input("Nilai Ujian : "))

# Proses perhitungan nilai murni
nilai_murni_keaktifan = nilai_keaktifan * 0.2
nilai_murni_tugas = nilai_tugas * 0.5
nilai_murni_ujian = nilai_ujian * 0.3

# Perhitungan nilai akhir
nilai_akhir = nilai_murni_keaktifan + nilai_murni_tugas + nilai_murni_ujian

# Output hasil
print("\nSiswa yang bernama", nama_siswa)
print("Dengan Nilai Persentasi Yang dihasilkan:")
print("Nilai Keaktifan * 20% :", nilai_murni_keaktifan)
print("Nilai Tugas * 50% :", nilai_murni_tugas)
print("Nilai Ujian * 30% :", nilai_murni_ujian)
print("Jadi Siswa yang bernama", nama_siswa, "memperoleh nilai akhir sebesar", nilai_akhir)