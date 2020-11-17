import random
from random import randint
import sys
import time
to_calc = []



def log(towrite):
	#Getting The First Number
	with open("log.txt", "r") as f:
		latest = f.readline()
		for latest in f:
			pass
	first = latest[0]
	# Adding 1
	try:
		first = int(first)
	except ValueError:
		print("Something Went Wrong. Check the log.txt file to make sure that the first character of the last line is a number.")
	numb = first+1
	numb = str(numb)


	#Log Time
	f = open("log.txt", "a")
	f.write(numb + ") " + towrite + "\n")
	f.close()

def rm_zero():
	with open("log.txt", "r") as f:
		lines = f.readlines()
		first = lines[0]
		delfirstline = True
		try:
			second = lines[1]
		except IndexError:
			delfirstline = False

		if (delfirstline == True) and (lines[0] == ("0" + "\n")):
			with open('log.txt', 'r') as f:
				data = f.read().splitlines(True)
			with open('log.txt', 'w') as f:
				f.writelines(data[1:])
			pass
		else:
			pass


# Start Program
while True:
	rm_zero()
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



	print("Welcome to the Main Menu!")
	print("You have 3 Choices:")
	print("")
	print("1) Start")
	print("2) View the Log")
	print("3) Exit the Program")
	print("")
	print("To Select an Option, Please Click the Number and Click Enter")
	print("For Example, to Start the Program, Press '1' Then 'Enter'")
	print("***" *7)
	keyboard_type = input()


	# Program
	if keyboard_type == '1':
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


	# View the log
	elif keyboard_type == '2':
		print("***" *7)	
		log("The Log Was Viewed")
		rm_zero()
		f = open("log.txt")
		lines = list(f)
		for line in lines:
			print(line, end="\r")
		sys.exit(0)

	#Exit
	elif keyboard_type == '3':
		print("BYEEEEEE!")
		log("You exited the program")
		rm_zero()
		sys.exit(0)

	else:
		print("Not A Valid Choice")
		print("Exiting the Program")
		log("You Made An Invalid Choice")
		rm_zero()
		sys.exit(0)



	# Program Finish
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
	average = str(average)
	log("The Average Was " + average)


	print("Your Average is... " + average + "!")
	rm_zero()
	sys.exit(0)
