import random

print("Your choices : 1.Rock 2.Paper 3.Scissors ")
lst_choices=['Rock','Paper','Scissors']


your_choice=int(input("Enter your choice from(1-3): "))
computer_choice=random.randint(1,3)
print("Your choice is :",lst_choices[your_choice-1])
print("Computer choice is : ",lst_choices[computer_choice-1])
      
if your_choice==computer_choice:
    print("It's tie")
elif (your_choice==3 and computer_choice==2 or your_choice==2 and computer_choice==1 or your_choice==1 and computer_choice==3):
    print("You Win")
else:
    print("Computer Win")
