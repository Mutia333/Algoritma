#Nama  : Mutia Ramadani (D0425333)
#Kelas : Sisfo B

# ---Tuple---

#Nama-nama musim
seasons = ("Spring", "Summer", "Autumn", "Winter")

# Menampilkan seluruh isi tuple
print("Daftar musim:", seasons)

# Mengakses elemen tertentu
print("Musim pertama:", seasons[0])
print("Musim terakhir:", seasons[-1])

# Menampilkan setiap musim dengan loop
print("\nMenampilkan musim satu per satu:")
for season in seasons:
    print("-", season)

# Contoh penggunaan tuple dalam kondisi
musim_favorit = "Spring"
if musim_favorit in seasons:
    print(f"\nMusim favoritku adalah {musim_favorit}!")
else:
    print("\nMusim favorit tidak ditemukan dalam tuple.")