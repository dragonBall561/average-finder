import random
from random import randint
import sys
import time
to_calc = []

while True:
	print("Hello, Welcome to...")

	print("                   ____   ____              _____       ____   ")
	print("    /|   |    /   /      /    |     /|     /     |     /       ")
	print("   / |   |   /   /__    /     /    / |    /           /__      ")
	print("  /__|   |  /   /      /_____/    /__|   /  ____     /         ")
	print(" /   |   | /   /      /     |    /   |  |  /   /|   /          ")
	print("/    |   |/   /____  /      |   /    |  |_____/ /  /_____      ")

	print("      ______    ______                ___        ____    ____  ")
	print("     /            /       /|    /    /   |      /       /    | ")
	print("    /            /       / |   /    /    |     /__     /     / ")
	print("   /____        /       /  |  /    /     |    /       /_____/  ")
	print("  /            /       /   | /    /     /    /       /     |   ")
	print(" /         ___/___    /    |/    /_____/    /____   /      |   ")


	print("To Start, Please Click Enter")
	print("To View the log, please write 'log' then click enter")
	print("If you got here by mistake type anything except log or nothing and then click enter")
	
	print("***" *7)
	keyboard_type = input()
	if keyboard_type == '':
		while True:
			print("Please type your number, then click enter.") 
			print("When you are done, type '00', then click enter")
			print("***" *7)
			keyboard_type = input()
			print("***" *7)
			print("")
			if keyboard_type == '00':
				break
			else:
				try:
					keyboard_type = float(keyboard_type)
				except ValueError:
					print("This is not a number!")
					to_calc.append(keyboard_type)
	elif keyboard_type == 'log':
		print("***" *7)	
		f = open("log.txt")
		lines = f.readlines()
		for line in lines:
			print(line)
		f.close()
		
		f = open("log.txt", "a")
		# Log Writing
		# Getting Latest Entry
		with open("log.txt", "r") as file:
			latest = file.readline()
			for latest in file:
				pass

		# Adding 1
		first = latest[0]
		first = int(first)
		write = first+1

		#Back to `str`
		write = str(write)

		#Log Time
		f = open("log.txt", "a")
		f.write(write + ") You have viewed the log now you are done! \n")
		f.close()
		sys.exit(1)


	else:
		print("BYEEEEEE!")

		# Log Writing
		# Getting Latest Entry
		with open("log.txt", "r") as file:
			latest = file.readline()
			for latest in file:
				pass

		# Adding 1
		first = latest[0]
		first = int(first)
		write = first+1

		#Back to `str`
		write = str(write)

		#Log Time
		f = open("log.txt", "a")
		f.write(write + ") Project Closed with exit code 1 \n")
		f.close()
		sys.exit(1)



	print("Okay, Getting Your Average! Please Wait!")
	# Put time thing here
	average = 0
	average = float(average)

	# Here be Dramatic Effects...
	for x in range (0,4):  
		b = "Adding Your Numbers" + "." * x
		print (b, end="\r")
		time.sleep(1)
	print("")



	# CODE
	for i in to_calc:
		average += i
		average = float(average)




	# Here be Dramatic Effects...
	for x in range (0,4):  
		b = "Dividing Your Numbers" + "." * x
		print (b, end="\r")
		time.sleep(1)
	print("")



	# CODE
	average /= len(to_calc)




	# Here be Dramatic Effects...
	for x in range (0,4):  
		b = "Writing to Log" + "." * x
		print (b, end="\r")
		time.sleep(1)
	print("")



	#CODE
	with open("log.txt", "r") as file:
		latest = file.readline()
		for latest in file:
			pass

	first = latest[0]
	first = int(first)
	write = first+1

	average = str(average)
	write = str(write)

	f = open("log.txt", "a")
	f.write(write + ") Success! The Number was " + average + "\n")
	f.close()

	average = str(average)
	print("Your Average is... " + average + "!")
	sys.exit(0)