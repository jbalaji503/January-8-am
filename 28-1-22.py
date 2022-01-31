#area of rectangle l * b
#perimeter of rectange 2l + 2b

#length = 10
#bre = collect it from user as floating number

#calculate area and perimeter
#print the output (integer)

length = 10

breadth = float(input("please enter breadth (float value): "))

Area = length * breadth
perimeter = 2 * (length + breadth)

print(Area)
print(perimeter)

#formatted output
print("the Area of rectangle is ",int(Area))
print("the perimeter of rectangle is ",int(perimeter))

print(f"the Area of rectangle is {int(Area)}")
print(f"the perimeter of rectangle is {int(perimeter)}")

#format
print("the Area of rectangle with length {} and breadth {} is {} ".format(length, breadth,int(Area)))
print("the perimeter of rectangle with length {} and breadth {} is {} ".format(length, breadth,int(perimeter)))


#calculate perimeter of circle with radius 10.2

radius=10.2
pi=3.14
perimeter=2*(pi*radius)

print("the perimeter of the circle is",(perimeter))

#calculate area of circle with radius (float)(collect using input function)
#calculate perimeter of circle with radius(float)(collect it through input function)

radius=float(input("please enter radius(float value)"))
pi=3.14
area=pi*radius*radius
perimeter=2*(pi*radius)

print("the area of circle is",int(area))
print("the perimeter of circle is",int(perimeter))

#collect radius and height from user
#calculate area of the cone(area of cone=0.33*pi*r*r*h(int)

radius=2
height=3
pi=3.14
conearea=0.33*pi*radius*radius*height

print(int(conearea))
