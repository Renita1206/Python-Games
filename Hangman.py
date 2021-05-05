import random

lives=7
l=[]

def display(a):
    print(a)

def generateAns(w):
    a="_"*len(w)
    return a

def updateAns(c,w,ans):
    for i in range(len(w)):
        if(c==w[i]):
            ans=ans[0:i]+c+ans[i+1:]
    return ans

print("The Categories are:")
print("1.Countries")
print("2.Famous People")
choice=int(input("Choose a category \n"))
if(choice==1):
    l=["Spain","United_Kingdom","India","Italy","China","Japan","France"]
elif(choice==2):
    l=["Rafael_Nadal","Christopher_Nolan","Serena_Williams","Elon_Musk","Bill_Gates","Stephen_Curry","Michael_Jordan"]

while(True):
    lives=7
    word=random.choice(l).lower()
    answer=generateAns(word)
    while(lives>0):
        print(answer)
        c=input()
        if(word.find(c)>=0):
            answer=updateAns(c,word,answer)
            if(word==answer):
                print("You win")
                break
        else:
            lives-=1
            display(lives)
        print(answer)
    e=input("Press c to continue \n")
    if(e!="c"):
        break




    
