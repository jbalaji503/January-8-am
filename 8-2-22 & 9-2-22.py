#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
tup1=(1,4,5,6,7,8)
tup2=(5,6,7,8,9)
tup3=(tup1+tup2)

#Find the common elements between two tuples
common=(set(tup1)&set(tup2))
print(tuple(common))

#Concatenate both tuples and remove duplicates from tuple
print(tup3)
print(set(tuple(tup3)))

#Find the index value of 9 (after concatenation)
print(tup3.index(9))

#multiply above elements 3 times
print(tup1*3)



#Create two empty sets
b=set()
c=b
print(c)
print(b)

#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
set1=set()
set2=set()
set3={7,8,9,1,2,3,4,5,0}
set4={4,5,6,0}
set1.update(set3)
set2.update(set4)

#remove 8 from set 1 and set 2
#discard 0 from set1 and set2 
set1.remove(8)
set2.remove(8)
set1.discard(0)
set2.discard(0)
print(set1)
print(set2)
print(set1)
print(set2)

#check whether set2 is subset of set1 or no ?
print(set2.issubset(set1))

#check whether both have common elements are no ?
print(set1&set2)
print(list(set(set1)))
print(tuple(set(set1)))



#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
print(dict1)
a = dict1[3][0][0]
b = dict1[3][0][2]
c = dict1[3][0][4]
d = dict1[3][0][6]
e = dict1[3][0][8]
print(a+b+c+d+e)
a2 = dict1[3][2][0]
b2 = dict1[3][2][5]
c2 = dict1[3][2][4]
d2 = dict1[3][2][3]
e2 = dict1[3][2][2]
print(a2+b2+c2+d2+e2)

#print all keys in dictionary and convert it into tuple
print(dict1.keys())
print(tuple(dict1.keys()))

#Find the average of all numbers available under key "2"
a = dict1[2][0]
b = dict1[2][1]
c = dict1[2][2]
print((a+b+c)/3)

