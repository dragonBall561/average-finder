import random
from random import randint
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
		else:
			pass


	print("Okay, Getting Your Average! Please Wait!")
	# Put time thing here
	average = 0
	average = float(average)

	for x in range (0,4):  
		b = "Adding Your Numbers" + "." * x
		print (b, end="\r")
		time.sleep(1)

	for i in to_calc:
		average += i
		average = float(average)

	for x in range (0,4):  
		b = "Dividing Your Numbers" + "." * x
		print (b, end="\r")
		time.sleep(1)

	average /= len(to_calc)

	average = str(average)
	print("Your Average is... " + average + "!")
	break