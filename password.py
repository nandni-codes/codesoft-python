password =input("Enter the password :  ")
upper = lower = digit = special_flag = False
special ='!@#%&*'
for ch in password:
    if ch.isupper():
        upper =True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit =True
    elif ch in special:
        special_flag =True
    else:
        print("wrong password")
if upper and lower and digit and special_flag :
    print("strong password")
else:
    print("weak password")