import random
import sys
import psutil
import os

path=input("Enter the path that the code is located in, example- C:\\Users\\Name\\Desktop\\CharacterGen : ")
path1=path + "\\Names.txt"
path2=path + "\\Emotions.txt"
path3=path + "\\Nouns.txt"
print("\n")

num=input("Enter how many character prompts you desire: ")
print("\n")

while int(num) <= 0:# loop until a valid number is entered
    num=input("Enter how many character prompts you desire above zero: ")
    print("Invaild value entered")

try:# try catch incase the filepath is wrong
    txt1=open(path1,"r")
    txt2=open(path2,"r")
    txt3=open(path3,"r")
except FileNotFoundError:
    print("File does not exist or folder not found.")
    exit()
    
m1=txt1.readlines()
m2=txt2.readlines()
m3=txt3.readlines()
l1=[]
l2=[]
l3=[]

for i in range(0,len(m1)-1):# I use 3 different for loops to easily see which list is beinging looped through and also the lists are different sizes
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
for j in range(0, int(num)):# output the desired number of prompts
    o1=random.choice(l1)# random choices from the list of nouns
    o2=random.choice(l2)
    o3=random.choice(l3)
    print(o1, "is feeling",o2, "because of her", o3)
txt1.close()# close files
txt2.close()
txt3.close()
