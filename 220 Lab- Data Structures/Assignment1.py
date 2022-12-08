import random
def randomNumber():
    lst = [item for item in input("Enter name of participants : ").split(', ')]
    while len(lst)!=1:
        no=random.randint(0,4)
        if no==1:
            index=len(lst)//2-1
            lst = lst[:index] + lst[index+1:]
            if len(lst)>1:
                print("The remaining players are: ", lst)
            else:
                print("The winner is: ", lst)
    return

randomNumber()


            
