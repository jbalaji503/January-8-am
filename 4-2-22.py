
#task 1

Get one string from user
identify the middle character of the string

a=input("please enter the string")
b=len(a)
c=b//2
print(c)

#Task 2

output: (strip,rstrip,lstrip method *)

b="******mission******"
print(b.strip("*"))
print(b.Istrip("*"))
print(b.rstrip("*"))     

#Task 3

collect three strings from user  name<space>float
string1: "ravi 10.30"  
string2: "meghala 12.19"
string3: "Gokul 20.20"
split + indexing
10.30 + 12.19 + 20.20 ===> output ===> add it 42.69

a = input("Enter the 1st name and float value")
b = input("Enter the 2nd name and float value")
c = input("Enter the 3nd name and float value")
a1=float(a.split()[1])
b1=float(b.split()[1])
c1=float(c.split()[1])
print(a1+b1+c1)

#Task 4

collect two strings from user
string1: python
String2: java
output ===> jythonpava64hv

a = input('enter the name of your country')
b = input('enter the name of your best cricketer')
c = (a.replace('i','v'))
d = (b.replace('v','i'))
e = len(a)
f = len(b)
print(c+d+str(e)+str(f)+(+a[3]+b[2]))

#Task 5

Collect two strings from user
string1: wikipedia
string2: typescript
output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
(ord , chr)

a=input('enter the green sity of india')
b=input('enter the capital of tamil nadu')
c=(ord('g'))
d=(ord('i'))
print(c+d)

#Task 6

collect one string from user:
string: computer
output: c6r
string: mathematics
output: m9s

a = input("Enter the capital of india")
b = a[0:1]
c = len(a[1:5])
d = a[5]
print(b+str(c)+d)





