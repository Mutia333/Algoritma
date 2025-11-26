#Nama  : Mutia Ramadani (D0425333)
#Kelas : Sisfo B 

## ---List ---

#Kumpulan data angka
data_angka = [1,2,3,4]
print(data_angka)

#Kumpulan data string
data_string = ["Aple","Lemon","Mango","Leci"]
print(data_string)

#Kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

#Kumpulan data campuran
data_campuran = ["Spring", "Summer", "Autumn", "Winter"]
print(data_campuran)

#Cara membuat list
data_range = range(0,10,5)  # range(star,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#Membuat list dengan for loop, list pemahaman
list_pakai_for = [i**4 for i in range(0,10,)]
print(list_pakai_for)

#Membuat list pakai for pakai if
list_pakai_for_if = [i for i in range(0,10) if i != 9]
print(list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pakai_for_if)



