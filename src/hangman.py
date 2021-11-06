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
		self.gameIsFinished = False 

	def makeAGuess(self):
		guess = input("Make a Letter Guess - ")
		guess = guess.strip()
		if len(guess) > 1:
			return guess[len(guess)-1] # if user bymistakely types in more than one letter then it selects the last letter
		return guess # if user types only one letter

	def fillTheLetter(self,guess,display):
		for position in range(self.chosen_word_length):
			letter = self.chosen_word[position]
			if letter == guess:
				display[position] = letter
		self.displayMessage(display)

	def displayMessage(self,display):
		print(" ".join(display))

	def isAllBlanksFilled(self,display):
		if "_" not in display:
			self.gameIsFinished = True
			print("You Win the hangman game")

	def drawHangmanArt(self,lives):
		print(stages[lives])

	def completedLetter(self,display):
		numOfBlanks = display.count("_")
		filledCharacter = self.chosen_word_length - numOfBlanks
		self.displayMessage(display)
		print(f"You have guessed {filledCharacter} words out of {self.chosen_word_length} words")

	def isLifeFinished(self,lives,display):
		if lives == 0:
			print("You Lose the hangman game")
			self.gameIsFinished = True
			self.completedLetter(display)

	def play(self):
		print(logo)
		print("-" * 50)
		print(f"You have only {self.lives} lives to complete the game")
		print("the word is ",self.chosen_word)
		display = ['_'] * self.chosen_word_length
		
		while not self.gameIsFinished:
			guess = self.makeAGuess()
			if guess in display: # guessed letter already exists
				print(f"You already have guessed {guess}. Try some different letter")
				continue
		
			# guessed letter is unique
			if guess in self.chosen_word:
				self.fillTheLetter(guess,display) # fill the guessed letter in the blanks and display 
				#self.displayMessage(display)
				self.isAllBlanksFilled(display)
			else:
				self.lives -= 1
				print(f"You guessed {guess}, that's not in the word. You lose a life.     Remaining Lives : {self.lives}")
				self.drawHangmanArt(self.lives)
				self.isLifeFinished(self.lives,display)

hg = hangman()
hg.play()