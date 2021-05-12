import random
import speech_recognition as sr
import pyttsx3

listener=pyttsx3.init()
r=sr.Recognizer()

l=["rock","paper","scissor"]
sysscore=0
userscore=0


while sysscore<5 and userscore<5:
    s=random.choice(l)
    u="mk"
    while(u not in "rock paper scissors"):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening")
                listener.say("Rock, paper, scissors")
                listener.runAndWait()
                audio = r.listen(source)
                print("Recognizing")
                command = r.recognize_google(audio)
                u = command.lower()
        except sr.UnknownValueError:
            print("unknown error occured")

        except Exception as e:
            print("Error \n", e)

    listener.say("Computer played"+s)
    listener.runAndWait()
    print("You played:      ",u)
    print("Computer played: ",s)
    if(u==s):
        continue
    elif u=="rock":
        if s=="scissor":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
        listener.say("Score: "+str(userscore)+"  "+str(sysscore))
        listener.runAndWait()
    elif u=="scissor":
        if s=="paper":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
        listener.say("Score: "+str(userscore)+" . "+str(sysscore))
        listener.runAndWait()
    elif u=="paper":
        if s=="rock":
            userscore+=1
            print("Your point")
        else:
            sysscore+=1
            print("System's point")
        listener.say("Score: "+str(userscore)+" . "+str(sysscore))
        listener.runAndWait()
    else:
        print("Invalid input")

    print("User: ",userscore,"\t System: ",sysscore)


listener.say("Game Over")
listener.runAndWait()
if(userscore>sysscore):
    listener.say("you won")
    listener.runAndWait()
    print("You win")
else:
    listener.say("you lost")
    listener.runAndWait()
    print("You lost")
