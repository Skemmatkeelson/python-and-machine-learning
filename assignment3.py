#a program that takes the height and width of a rectangle and computes the area and perimeter

#takes and converts the values into integer
width=int(input("enter the value for the width: "))
height=int(input("enter the value for the height: "))

#computes area
print(f"the area of the rectangle with height {height} and width {width} is {height*width}")

#computes perimeter
print(f"the perimeter of the rectangle with height {height} and width {width} is {2*(width+height)}")