# ==================================
# PROGRAM TABEL DATA MAHASISWA
# INPUT - PROCESS - OUTPUT
# ==================================

# INPUT
jumlah_data = int(input("Masukkan jumlah mahasiswa: "))

data_mahasiswa = [Data Mahasiswa ke-1
NIM   : 001
Nama  : Andi
Nilai : 85

Data Mahasiswa ke-2
NIM   : 002
Nama  : Budi
Nilai : 90

Data Mahasiswa ke-3
NIM   : 003
Nama  : Citra
Nilai : 88]

# PROCESS
for i in range(jumlah_data):
    print(f"\nData Mahasiswa ke-{i+1}")

    nim = input("NIM   : ")
    nama = input("Nama  : ")
    nilai = input("Nilai : ")

    data_mahasiswa.append([nim, nama, nilai])

# OUTPUT
print("\n" + "=" * 40)
print("{:<10} {:<15} {:<10}".format("NIM", "NAMA", "NILAI"))
print("=" * 40)

for baris in data_mahasiswa:      # Loop luar
    for kolom in baris:           # Loop dalam (nested loop)
        print("{:<15}".format(kolom), end="")
    print()

print("=" * 40)