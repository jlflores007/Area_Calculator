import math 

#Area Calculator

# 1) Triangle
# 2) Rectangle
# 3) Square
# 4) Circle
# 5) Quit

print("===================\nArea Calculator 📐\n===================")


user = int(input("1)Triangle\n2)Rectangle\n3)Square\n4)Circle\n5)Quit\n\nWhich Shape: "))


if user == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = (height * base) / 2
    print("The area is ", area)
elif user == 2:
    length = int(input("Lenght:"))
    width = int(input("Width: "))
    area = length * width
    print("The area is ", area)
elif user == 3:
    side = int(input("Side: "))
    area = side ** 2
    print("The area is ", area)
elif user == 4:
    radius = int(input("Radius: "))
    area = math.pi * radius ** 2
    print("The area is ", area)
elif user == 5:
    print("Bye")

else:
    print("Something is wrong...")



