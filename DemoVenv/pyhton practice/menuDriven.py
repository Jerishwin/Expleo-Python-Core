def circle(radius):
    print("Area of Circle: ",3.14*radius*radius)

def rectangle(length,breadth):
    print("Area of rectangle: ",length*breadth)

def suare(side):
    print("Area of suare: ",side*side)

while True:
    print("Menu")
    print("1. Circle")
    print("2. Rectangle")
    print("3. suare")
    print("4. exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        radius = int(input("Enter radius: "))
        circle(radius)
    elif choice==2:
        length = int(input("Enter length: "))
        breadth = int(input("Enter dreadth: "))
        rectangle(length,breadth)
    elif choice==3:
        side = int(input("Enter side: "))
        suare(side)
    elif choice==4:
        break
    else:
        print("rong choice")