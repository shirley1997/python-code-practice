import random
play=True
while play:
    secret = random.randint(1,10)

    print('----------welcome to the game!-------------\n')
    print('guess which number I\'m thinking!!')

    temp=input('please type the number:')
    guess=int(temp)

    while guess!=secret:
        if guess>secret:
            print("it's bigger than the number!\n")
        else:
            print("it's smaller than the number!\n")
        temp=input('you\'re wrong,pls guess again:\n')
        guess=int(temp)

    if guess==secret:
        print("correct!you\'re awesome!")
    selecting= True  ###赋值
    while(selecting):
        name=input('do you wanna play this game again?type yes or no:\n')
        word=name
        if word=='yes':
            print('ok,let us play again!')
            selecting=False
            
        elif word == 'no':
            print('game over!')
            selecting=False
            play=False
        else:
            print("you can only type yes or no!")
          

