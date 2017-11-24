import random
playing = True
while playing:
    secret = random.randint(1,10)
    print('------------welcome to the game!!!-------------')
    temp = input('please type the number:\n')
    guess=int(temp)

    while guess!=secret:
        if guess>secret:
            print('it\'s bigger than the number,guess again!:\n')
        else:
            print('it\'s smaller than the number,guess again!:\n')
        temp=input()
        guess=int(temp)

    if(guess==secret):
        print('correct!you\'re awesome!')

    selecting=True
    while selecting:
        
            name=input('do you wanna play again?type yes or no :\n')
            word=name
            if word == 'yes':
                print('ok,let\'s play again!')
                selecting=False

            elif word == 'no':
                print('game over!')
                selecting=False
                playing=False
            else:
                print('you can only type yes or no!')
