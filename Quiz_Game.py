print("Welcome to my Computer Quiz")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
questions = 0

answer = input("What does CPU stands for? ")
questions +=1
if answer.lower() == "central processing unit":
    print("Excellent! Your answer is correct")
    score +=1
else:
    print("Oh no! The answer is incorrect")

answer = input("What does GPU stands for? ")
questions +=1
if answer.lower() == "graphics processing unit":
    print("Excellent! Your answer is correct")
    score +=1
else:
    print("Oh no! The answer is incorrect")

answer = input("What does RAM stands for? ")
questions +=1
if answer.lower() == "random access memory":
    print("Excellent! Your answer is correct")
    score +=1
else:
    print("Oh no! The answer is incorrect")

answer = input("What does ROM stands for? ")
questions +=1
if answer.lower() == "read only memory":
    print("Excellent! Your answer is correct")
    score +=1
else:
    print("Oh no! The answer is incorrect")

print("Your test is completed")
print("You got " + str(score) + " questions correct")
print("You got " + str((score/questions)*100) + "%.")