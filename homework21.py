print("i can solve ax^2 +bx+c for you")
while True:
    try:
        a = float(input("What is the value of a?:"))
        b = float(input("What is the value of b?:"))
        c = float(input("What is the value of c?:"))
        if a == 0:
            print("a cannot be zero")
        else:
            break

    except:
        print("sorry that is not a valid number")

discriminant = (b**2-4*a*c)

while discriminant < 0:
    print("the quadratic does not have real roots ")
    a = float(input("What is the value of a?:"))
    b = float(input("What is the value of b?:"))
    c = float(input("What is the value of c?:"))

if discriminant == 0:
    x =  -b/(2*a)
    print("the root is: ", x)
else:
    x1 = (-b + (discriminant)**0.5) / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    print("The roots are: ")
    print(x1)
    print(x2)

quit()







