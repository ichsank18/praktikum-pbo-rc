jumlah=int(input("Masukan Jumlah Data Mahasiswa : "))

Mahasiswa={}

print('\n')
for i in range(jumlah):
    n=str(input("Masukan Nama Mahasiswa  :"))
    nil=int(input("Masukan Nilai Mahasiswa  :"))
    Mahasiswa[n]=nil 
    print("\n")
    
print("Data Mahasiswa : ", Mahasiswa)