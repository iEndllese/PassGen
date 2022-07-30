import random
import config
import time

print(config.BANNER)

# Entering password information
KolPass = input("Введите количество паролей: ")
DlinPass = input("Введите длину паролей: ")

# Convert to int
KolPass = int(KolPass)
DlinPass = int(DlinPass)

# Creating a new file
file = open("New_genpass.txt", "w+")


# Password generation cycle
for i in range(KolPass):
	password = ""

	for n in range(DlinPass):
		password += random.choice(config.chorse)
	
	file.write(password + "\n")
	time.sleep(00.03)
	print(password)

file.close()
print("Готово!")
input()
	
