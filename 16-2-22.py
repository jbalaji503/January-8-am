#Task1:
'''Using Range function  print multiples of 5 from 0 to 75
Using Range function  print multiples of 8 from 0 to 72
Using Range function  print multiples of 5 from 75 to 0
Using Range function  print multiples of 8 from 96 to 72'''

'''for i in range(0,75):
    if i % 5 == 0:
        print(i)
for i in range(0,72):
    if i % 8 == 0:
        print(i)
for i in range(75,0):
    if i % 5 == 0:
        print(i)
for i in range(96,72):
    if i % 8 == 0:
        print(i)'''


#Task3:

'''Get a dynamic dictionary from user
clues Task2 and Task3
1. get number of elements from user
Loop through range
append to list/dicti'''


'''dic1 = {}
n = int(input('enter number of items:'))
for i in range(n):
    key, value = input().split()
    dic1[key] = value
print(dic1)


a=['name','age']
d = {}
for i in a:
    j = input("Enter Name of key")
    d[i]=j   
print("Dictionary is : ",d)'''
     

#Task4:

'''Get two integers from user
print multiples of 8 between them
clues:
Use range function in for loop
Use if condition inside for loop
add in to list

input 10 100
multiples of 8

[16,24,32.....,96]'''

'''a = int(input('enter two integers'))
for i in range(a):
     if i % 8 == 0:
         print(i)'''
     

#Task5:


'''Input:
Li1 = [3,4,5,2,7,8,9,10]

Output:
Li_odd = [3,5,7,9]
Li_even = [4,2,8,10]

#Li1 = [3,4,5,2,7,8,9,10]'''

'''li1 = []
n = int(input('enter number of elements:'))
for i in range(1, 1+n):
     allelements = int(input('enter element:'))
     li1.append(allelements)
even = []
odd = []
for j in li1:
     if j % 2== 0:
          even.append(j)
     else:
          odd.append(j)
print('Li_even = ',even)
print('Li_odd = ',odd)'''
     
               
#Task6:

'''Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
Output:
neg_LI = [-1,-7,-3]
pos_LI = []
Zeros = []

Numeber of postivie ele: 7
Number nega: 3
Number of zeros: 2'''

'''li2 = []
n = int(input('enter number of elements:'))
for i in range(1, 1+n):
     allelements = int(input('enter element:'))
     li2.append(allelements)
positive = []
negative = []
zeros = []
for j in li2:
     if j>0:
          positive.append(j)
     elif j<0:
          negative.append(j)
     elif j>=0:
          zeros.append(j)
print('pos_LI = ',positive)
print('neg_LI = ',negative)
print('Zeros = ',zeros)'''

#Task7:

#Study range function and for loop properly

'''print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))'''

