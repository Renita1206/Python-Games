import random

l=["rock","paper","scissor"]
sysscore=0
userscore=0
while sysscore<5 and userscore<5:
    s=random.choice(l)
    u=input("Enter rock, paper or scissor: ")
    print("System played               :",s)
    if(u==s):
        continue
    elif u=="rock":
        if s=="scissor":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
    elif u=="scissor":
        if s=="paper":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
    elif u=="paper":
        if s=="rock":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
    else:
        print("Invalid input")

    print("User: ",userscore,"\t System: ",sysscore)

print("Game Over")
if(userscore>sysscore):
    print("You win")
else:
    print("You lose")
