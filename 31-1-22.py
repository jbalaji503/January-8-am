#collect length , breadth , height from user (all of them in float datatype)
#calculate area of geometry : (length * breadth) + (length * height)
#Expected output:The Area of Geometry with length {} , breadth {} and height {} is {}

(length)= float(input("please enter the length"))
(breadth)= float(input("please enter the breadth"))
(height)= float(input("please enter the height"))
geometryarea=(length*breadth)+(length*height)

print(geometryarea)
print("the area of geometry with length {} and breadth {} and height {} is {}".format(length,breadth,height,int(geometryarea)))
