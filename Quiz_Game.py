print("Welcome to my Quiz Game!")

playing = input("Do you want to play? Enter yes or no .... ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's get started :)")
score = 0

answer = int(input("How many countries in the world ? "))
if answer == 195:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what's the biggest country in the world? ")
if answer.lower() == "russia":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What country has the largest population? ")
if answer.lower() == "china":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the longest river in the world? ")
if answer.lower() == "nile":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")