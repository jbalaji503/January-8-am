#Task3

#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

a = int(input("Get one number from user"))
if a%3:
    print("entering into if scope")
    print('Fizz')
elif a%5:
    print('buzz')
elif a%(3 and 5):
    print('Fizzbuzz')
else:
    print("entering into else scope")
    print('invalidnumber')


#Task4:

#Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL


n = int(input("Get one mark from student"))
if (n>0 or n<100):
    print("entering into if scope")
    print("validnumber")
elif n>50:
    print('Pass')
elif (n>90 or n<100):
    print('A')
elif (n>80 or n<89):
    print('B')
elif (n>70 or n<79):
    print('C')
elif (n>60 or n<69):
    print('D')
elif (n>50 or n<59):
    print('E')
else:
    print("entering into else scope")
    print('Fail')
    

   
#Task 5:

#collect three marks from user
#calculate mark1 + mark2 + mark3 / 100

#if calculate > 90 ===> Grade A
#if calculate > 75 ==> Grade B
#calculate > 50  ==> grade C
#Other wise ===> Grade D


mark1 = int(input("enter the marks"))
mark2 = int(input("enter the marks"))
mark3 = int(input("enter the marks"))
totalmarks =int(mark1+mark2+mark3)
avgmarks =(totalmarks/3)
if avgmarks>90:
    print("entering into if scope")
    print("Grade A")
if avgmarks>75:
    print("Grade B")
if avgmarks>50:
    print("Grade C")
else:
    print("entering into else scope")
    print("Grade D")
    

    



