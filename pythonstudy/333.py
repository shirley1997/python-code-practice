import random

playing = True;
while (playing) :
	secret = random.randint(1,10)
	print('---Welcome to the game!!!---')
	temp = input('guess which number between 1 to 10 I\'m thinking!:\n')
	guess = int(temp)
	while(guess != secret) :
		if guess>secret:
			print("it's bigger than the answer!")
		else:
			print("it's smaller than the answer!")
		temp = input('you\'re wrong, type again!\n')
		guess = int(temp)
		
	print('correct! you\'re awesome!')
	selecting = True
	while (selecting):
            
		choice = input('wanna play again?')
		if choice == 'yes':
			print('ok! let\'s play another round!')
			selecting = False
		elif choice == 'no':
			print('ok, then game over!')
			playing = False
			selecting = False
		else:
			print('you can only type yes or no!')
