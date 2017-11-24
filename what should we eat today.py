import random
name=input('what\'s your name?\n')
print('hello! ',name)

playing= True
ok=True
name=input('are you hungry right now?type yes or no\n')
word=name
if word == 'yes':
    print('then what should we eat today?do you have any idea?')
elif word == 'no':
    name=input('but I\'m really hungry right now...pls think about it!:')
    word=name
    if word == 'no':
        print('fine...I\'m so sad...')
        ok=False
        playing=False
    else:
        print('yeahhh!!\n')
        
    
else :
    name=input("hey I'm talking to you!yes or no?\n")
    word=name
    if word=='yes':
        print('ok!!')
    else:
        print('ok...bye')
        playing=False

while (playing):
    
    secret = random.randint(1,5)
    name=input('I can give you some advice:\n1.milk cake\n2.fish\n3.chicken\n4.rice\n5.beef steak\nyou can just type the number:\n')
    choice=int(name)

    while choice!=secret:
        print('I don\'t wanna eat it...do you have better idea?')
        name=input('type the number:\n')
        choice=int(name)

    if(choice == secret):
        print('ok let\'s go to eat it!!!')

    selecting=True
    while selecting:
        name=input('or what else do you want to eat?type yeah or nothing else:\n')
        word=name
        if word == 'nothing else':
            print('ok game over!')
            selecting=False
            playing=False
        elif word == 'yeah':
            print('ok then look at the advice!')
            selecting=False
        else:
            print('you can only type nothing else or yeah...\n')
            
          
