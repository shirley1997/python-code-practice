pyg = 'ay'

original = input("please enter a name: ")
word = original.lower()
first = word[0]
new_word = word[1:] + first + pyg

if len(new_word)>0 and new_word.isalpha():
        print (new_word)
else:
        print (empty)
