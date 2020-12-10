def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def bagi(x,y):
    return x / y

def kali(x,y):
    return x * y

print("Pilih operasi yang anda inginkan : \n 1. Tambah \n 2. Kurang \n 3. Kali \n 4. Bagi") 

pilihan = input("masukan pilihan anda 1/2/3/4 : ")

angka1 = float(input("masukan angka pertama : "))
angka2 = float(input("masukan angka kedua : "))

if pilihan == '1':
    print (tambah(angka1,angka2))

if pilihan == '2':
    print (kurang(angka1,angka2))

if pilihan == '3':
    print (bagi(angka1,angka2))

if pilihan == '4':
    print (kali(angka1,angka2)) 