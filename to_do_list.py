tasks=[]
while True:
    num=int(input("Enter choice: "))
    if num==1:
     task=input("Enter the tasks: ")
     tasks.append(task)
    elif num==2:
        task=input("Enter the remove tasks: ")
        if task in tasks:
            tasks.remove(task)
    elif num==3:
        print("Enter task is :",tasks)
    elif num == 4:
        break
    
    
    
