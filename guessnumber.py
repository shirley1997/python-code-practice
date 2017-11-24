import random;
s = int(random.uniform(1,10));
m = int(input("type the number: \n"));

while(m!=s):
    if(m<s):
        print("too small!");
        m = int(input("type other number: \n"));
    if(m>s):
        print("too big!");
        m = int(input("type other number: \n"));
    if(m ==s):
        print("correct!");
        break;
