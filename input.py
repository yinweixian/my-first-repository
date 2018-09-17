import math
#calculate the area of a crcle
#radius*radius*pi
def areaOfCricle(radius1):
    pi=3.14159265
#get radius
    radius = radius1
#calculate the area
    radius = float(radius)
    area=radius*radius*pi
#display the area
    print("the area of the circle is: ",area)


#radiusx=input("what is the radius")
#areaOfCrcle(radiusx)

def pythagoras_theorem(ax,bx):
    #a^2+b^2=c^2
    a=float(ax)
    b=float(bx)
    c=a*a+b*b
    c=math.sqrt(c)
    print("the third side is",c)


#ax=input("enter the first side of the triangle")
#bx=input("enter the second side of the triangle")
#pythagoras_theorem(ax,bx)


def add_numbers():
    num1 = input("enter a number")
    num2 = input("enter a second number")
    num3 = int(num1)+int(num2)
    return num3
num4=add_numbers()
print("the sum of your numbers is")
print(num4)

#print("you are number",11437,"your name no longer matters. You work for us, under the direct command of",18362)
