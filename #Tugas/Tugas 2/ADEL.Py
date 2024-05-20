def hitung_rata_rata(tugas1, tugas2, tugas3):
    return (tugas1 + tugas2 + tugas3) / 3

print("PROGRAM HITUNG NILAI RATA-RATA")
nim = input("Nim Siswa : ")
nama = input("Nama Siswa : ")
tugas1 = float(input("Nilai Tugas I : "))
tugas2 = float(input("Nilai Tugas II : "))
tugas3 = float(input("Nilai Tugas III : "))

rata_rata = hitung_rata_rata(tugas1, tugas2, tugas3)

print("\nLayar Keluaran")
print("Nim", nim, "Siswa yang bernama", nama)
print("Memperoleh nilai rata-rata", rata_rata, "dari hasil tugas yang diikutinya.")
input("\nTekan enter untuk keluar...")