# Import datetime library
import datetime

# Get today's date
date = datetime.datetime.today().strftime("%d %B, %Y")

# Testing
#print(date)

# Print Welcome Message
msg = print("Oh Hi! Welcome to my game, DORK\nIn short, it's a zork-like game\nI need to grab some info from you to complete the story, Okay?")

# Take Data From User
boy = input("\nBoy's Name: ")
girl = input("Girl's Name: ")

# Added decision in functions to call it later
def decision2Yesfunction():
    decision2 = input(f"\n--\n\nWhile walking in the street you found a pretty girl, wait a minute she is {girl},  - Talk to her ? - Yes Or No: ")
    if decision2.lower() == "yes" :
        print("— Good!")
        decision3Yesfunction()
    if decision2.lower() == "no" :
        print("— Well, you just have done my demo")
def decision2Nofunction():
    decision2 = input(f"\n--\n\nWhile walking in the street you found a pretty girl, wait a minute she is {girl},  - Talk to her ? - Yes Or No: ")
    if decision2.lower() == "yes" :
        print("— Good!")
        decision3Nofunction()
    if decision2.lower() == "no" :
        print("— Well, you just have done my demo")

def decision3Yesfunction():
    decision3 = input(f"\n--\n\n{girl} seems she in a bad mood, and oh, you have the flower remember? - Give it to her ? - Yes Or No: ")
    if decision3.lower() == "yes" :
        print("— Okay, she seems in a good mood now, and you got the good ending :)\n\n----The END---\n\n")
    if decision3.lower() == "no" :
        print("— Okay, she seems in a good mood now, and you got the bad ending :(\n\n----The END---\n\n")
def decision3Nofunction():
    print(f"\n--\n\n{girl} seems she in a bad mood and oh you left the flower")
    print("— Okay, she seems in a good mood now, and you got the bad ending :(\n\n----The END---\n\n")

decision1 = input(f"\n\n----The Story---\n\nAt {date}. {boy} while walking on the street he found a flower on the road - Take It ? - Yes Or No: ")
if decision1.lower() == "yes" :
    print("— Okay, you just picked it up!")
    decision2Yesfunction()
if decision1.lower() == "no" :
    print("— Okay, You Ignored it")
    decision2Nofunction()

# Finaly Message
print("Hope you liked my demo :D")

