list1 = ['my','love','is','you',100,2000];
list2 = ['nope','hahaha',299,380,280];

print("初始列表： ",list1);
list1[3]= "for";
print("第一次更新： ",list1);
list1.append(30000);
del list1[4]

print("第二次更新： ",list1);
print("list2[1:5]: ",list2[1:5]);

tup1 = (50,)*5;
tup2 = (100,1200,1002);
tup3 = tup1 + tup2;
print(tup1);
tup4 = (1,2,3,4);
for x in tup4:
    print(x);
