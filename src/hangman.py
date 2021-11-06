from hangman_art import logo, stages
from hangman_words import word_list
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class hangman():
	def __init__(self):
		self.chosen_word = random.choice(word_list)
		self.chosen_word_length = len(self.chosen_word)
		self.lives = len(stages) - 1
		self.game_is_finished = False 

	def make_a_guess(self):
		guess = input(bcolors.WARNING + "Make a Letter Guess - " + bcolors.ENDC)
		guess = guess.strip()
		if len(guess) > 1:
			# if user bymistakely types in more than one letter then it selects the last letter
			return guess[len(guess) - 1]
		return guess

	def fill_the_letter(self, guess, display):
		for position in range(self.chosen_word_length):
			letter = self.chosen_word[position]
			if letter == guess:
				display[position] = letter
		self.display_message(display)

	def display_message(self, display):
		print(bcolors.OKBLUE + " ".join(display) + bcolors.ENDC)

	def is_all_blanks_filled(self, display):
		if "_" not in display:
			self.game_is_finished = True
			print(bcolors.OKGREEN + "You Win the hangman game" + bcolors.ENDC)

	def draw_hangman(self, lives):
		print(bcolors.HEADER + stages[lives] + bcolors.ENDC)

	def completed_letter(self, display):
		num_of_blanks = display.count("_")
		filled_character = self.chosen_word_length - num_of_blanks
		self.display_message(display)
		print(bcolors.OKCYAN + f"You have guessed {filled_character} words out of {self.chosen_word_length} words" + bcolors.ENDC)

	def is_life_finished(self, lives, display):
		if lives == 0:
			print(bcolors.FAIL + "You Lose the hangman game" + bcolors.ENDC)
			self.game_is_finished = True
			self.completed_letter(display)

	def play(self):
		print(logo)
		print("-" * 50)
		print(bcolors.OKCYAN + f"You have only {self.lives} lives to complete the game" + bcolors.ENDC)
		display = ['_'] * self.chosen_word_length
		
		while not self.game_is_finished:
			guess = self.make_a_guess()
			if guess in display: 
				# guessed letter already exists
				print(bcolors.OKCYAN + "You already have guessed " + bcolors.WARNING + guess + bcolors.ENDC + bcolors.OKCYAN +  ". Try some different letter" + bcolors.ENDC)
				continue
		
			# guessed letter is unique
			if guess in self.chosen_word:
				# correct guess
				self.fill_the_letter(guess, display)
				self.is_all_blanks_filled(display)
			else:
				# wrong guess
				self.lives -= 1
				print(bcolors.FAIL + "You guessed " + bcolors.WARNING + guess + bcolors.ENDC + bcolors.FAIL + ", that's not in the word. You lose a life.\tRemaining Lives : " + bcolors.WARNING + str(self.lives) + bcolors.ENDC)
				self.draw_hangman(self.lives)
				self.is_life_finished(self.lives, display)

hg = hangman()
hg.play()