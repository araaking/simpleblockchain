import random 

karakter = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){|'~` "

while 1:
	pnjgn_pass = int(input("berapa panjang pasword yang mau kamu inginkan? : "))
	pasword_count = int(input("berapa banyak tipe password yang mau kita sarankan?"))
	for x in range(0,pasword_count):
		password = " "
		for x in range(0,pnjgn_pass):
			pass_char = random.choice(karakter)
			password = password + pass_char
		print("ini password mu " + password)