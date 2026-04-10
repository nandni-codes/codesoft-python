a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
while(True):
    Operation=int(input("Enter your choice of operation: "))
    if Operation==1:
        print(f"Addition of {a} + {b} is: ",a+b)
    elif Operation==2:
        print(f"Subtraction of {a} - {b} is: ",a-b)
    elif Operation==3:
        print(f"Multiplication of {a} X {b} is : ",a*b)
    elif Operation==4:
        print(f"Division of {a} / {b} is : ",a/b)
    else:
        break
        
        