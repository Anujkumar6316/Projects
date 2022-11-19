# date: 19nov 2022
# Anuj kumar
# project no: 01
# update no: 00

# IDEA
# step1: want to play?
# yes-> provide question, no-> quit()
# calculate score 
# provide with question

playing = input("Do u want to play? ")
if playing!='yes':
    quit()

print("Okay! let's play :)")
ans1 = int(input("20+30="))
score = 0
if(ans1==50):
    score+=4
else:
    score-=1

ans2 = int(input("20%50="))
if(ans2==0):
    score+=4
else:
    score-=1

ans3 = int(input("30//4="))
if(ans3==7):
    score+=4
else:
    score-=1

print(f"Congratulations! Your score is: {score} out of 12")
