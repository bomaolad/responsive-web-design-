####### Number Guessing Game ########
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
import random
attempts = 0
number = random.randint(1, 100)
print(f"Guessed number: {number}")

def game():
	global guess
	global attempts
	while guess != number:
		if guess > number:
			print("Too high")
			attempts -= 1
			print(f"You have {attempts} attempts remaining")
			if attempts > 0:
				guess = int(input("Guess again: "))
			else:
				print(f"You lose.")
				exit()
				
		elif guess < number:
			print("Too low")
			attempts -= 1
			print(f"You have {attempts} attempts remaining")
			if attempts > 0:
				guess = int(input("Guess again: "))
			else:
				print(f"You lose.")
				exit()
		
	else:
			print("Correct, you win")
			exit()
	
if difficulty == "easy":
	attempts = 10
	print(f"You have {attempts} attempts to guess the number")
	guess = int(input("Make a guess: "))
	game()
			
elif difficulty == "hard":
	attempts = 5
	print(f"You have {attempts} attempts to guess the number")
	guess = int(input("Make a guess: "))
	game()
