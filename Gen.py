import random


txt1=open("location of file of Names","r")
txt2=open("location of file of Emotions","r")
txt3=open("location of file of Nouns","r")
m1=txt1.readlines()# read the lines of the txt files
m2=txt2.readlines()
m3=txt3.readlines()
l1=[]# create lists
l2=[]
l3=[]
for i in range(0,len(m1)-1):# I use 3 different for loops to easily see which list is beinging looped through this can be optimized but the program is very small
    x=m1[i]
    z=len(x)
    a=x[:z-1]
    l1.append(a)
l1.append(m1[i+1])
for i in range(0,len(m2)-1):
    x=m2[i]
    z=len(x)
    a=x[:z-1]
    l2.append(a)
l2.append(m2[i+1])
for i in range(0,len(m3)-1):
    x=m3[i]
    z=len(x)
    a=x[:z-1]
    l3.append(a)
l3.append(m3[i+1])
for j in range(0, 9):# print ten prompts
    o1=random.choice(l1)
    o2=random.choice(l2)
    o3=random.choice(l3)
    print(o1, "is feeling",o2, "because of her", o3)# print the sentences
txt1.close()# close files
txt2.close()
txt3.close()
