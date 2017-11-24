import random
secret = random.randint(1,10)

print('-----------welcome to the game!!!-------------')
temp = input('guess which number between 1 to 10 I\'m thinking!:\n')
guess=int(temp)

if guess==secret:
        print('correct!you\'re awesome!')
while (guess != secret) :
    temp = input('you\'wrong,type again!\n')
    guess= int(temp)
    
        name = input('wanna play again?')
        word = name
        if word == 'yes':
            print('ok let\'s play another round!')
        elif word == 'no':
            print('ok,then game over!')
        else:
            print("you can only type yes or no!")
    else:
        if guess>secret:
            print("it's bigger than the answer!")
        else:
            print("it's smaller than the answer!")
###print('游戏结束，不玩啦！')
    

    
