from hangman_art import logo,stages
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
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class hangman():
	def __init__(self):
		self.chosen_word = random.choice(word_list)
		self.chosen_word_length = len(self.chosen_word)
		self.lives = len(stages) - 1
		self.game_is_finished = False 

	def make_a_guess(self):
		guess = input("Make a Letter Guess - ")
		guess = guess.strip()
		if len(guess) > 1:
			return guess[len(guess) - 1] # if user bymistakely types in more than one letter then it selects the last letter
		return guess # if user types only one letter

	def fill_the_letter(self, guess, display):
		for position in range(self.chosen_word_length):
			letter = self.chosen_word[position]
			if letter == guess:
				display[position] = letter
		self.display_message(display)

	def display_message(self, display):
		print(" ".join(display))

	def is_all_blanks_filled(self, display):
		if "_" not in display:
			self.game_is_finished = True
			print("You Win the hangman game")

	def draw_hangman(self, lives):
		print(stages[lives])

	def completed_letter(self, display):
		num_of_blanks = display.count("_")
		filled_character = self.chosen_word_length - num_of_blanks
		self.display_message(display)
		print(f"You have guessed {filled_character} words out of {self.chosen_word_length} words")

	def is_life_finished(self, lives, display):
		if lives == 0:
			print("You Lose the hangman game")
			self.game_is_finished = True
			self.completed_letter(display)

	def play(self):
		print(logo)
		print("-" * 50)
		print(f"You have only {self.lives} lives to complete the game")
		print("the word is ",self.chosen_word)
		display = ['_'] * self.chosen_word_length
		
		while not self.game_is_finished:
			guess = self.make_a_guess()
			if guess in display: # guessed letter already exists
				print(f"You already have guessed {guess}. Try some different letter")
				continue
		
			# guessed letter is unique
			if guess in self.chosen_word:
				self.fill_the_letter(guess, display) # fill the guessed letter in the blanks and display 
				#self.display_message(display)
				self.is_all_blanks_filled(display)
			else:
				self.lives -= 1
				print(f"You guessed {guess}, that's not in the word. You lose a life.     Remaining Lives : {self.lives}")
				self.draw_hangman(self.lives)
				self.is_life_finished(self.lives, display)

hg = hangman()
hg.play()