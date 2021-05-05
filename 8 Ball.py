import random

l=["Yes","No","Hell No","Maybe","Ask me later","Go for it","Are you insane??","YOLO"]
while(True):
    print("What do you want to ask?")
    inp=input()
    if(inp=="exit" or inp=="bye"):
        break
    else:
        print(l[random.randrange(0,8)])
        print("\n\n\n")