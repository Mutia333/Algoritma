#Nama  : Mutia Ramadani (D0425333)
#Kelas : Sisfo B

# Perbedaan List dan Tuple
# List = data yang bisa diubah
musim_list = ["Spring", "Summer", "Autumn", "Winter"]
# Tuple = data yang tidak bisa diubah
musim_tuple = ("Spring", "Summer", "Autumn", "Winter")

# Menampilkan isi list dan tuple
print("Isi List  :", musim_list)
print("Isi Tuple :", musim_tuple)

# Contoh akses elemen
print("\nAkses elemen ke-0:")
print("List  :", musim_list[0])
print("Tuple :", musim_tuple[0])

# Mengubah isi list (berhasil)
musim_list[1] = "Dry Season"
print("\nList setelah saya ubah elemen ke-1:", musim_list)

# Coba ubah tuple (error karena tuple tidak bisa diubah)
print("\nPercobaan ubah tuple:")
try:
    musim_tuple[1] = "Dry Season"
except:
    print("Tuple tidak bisa diubah (immutable).")

# Menambah data baru ke list
musim_list.append("Rainy")
print("\nList setelah saya tambah elemen baru:", musim_list)