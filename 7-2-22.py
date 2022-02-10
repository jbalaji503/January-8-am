#Create an empty list (two ways)

li1=[2,4,3,6,5]
li2=[]
li1.clear()
print(li1)
print(li2)

#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list

li1=[8,9,1,5,6,7,8,-1]
print(li1.count(8))
li1.sort()
print(li1)
li1.reverse()
print(li1)

#find sum (List) + min + Max 

li1=[8,9,1,5,6,7,]
print(sum(li1))
print(min(li1))
print(max(li1))

#remove duplicates from list and give output in the format of tuple

li1={8,9,1,5,6,7,8,8,2}
print(li1)
