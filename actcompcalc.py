#!/usr/bin/python
#Use this program to calculate your ACT composite score
#Version 2.1
mathScore = int(input('Type in your math score '))
englishScore = int(input('Type in your english score '))
readingScore = int(input('Type your reading score '))
scienceScore = int(input('Type your science score '))

#This calculates the composite score
compScore = float(mathScore + readingScore + englishScore + scienceScore)/float(4)

#Added Rounding Mechanism
print(round(compScore,0))


#This section of code offers the users feedback regarding their score
if compScore > 34:
	print("Welcome to the 99th Percentile. It's lonely at the top.")

if compScore > 32 and compScore < 34:
	print("You must be aiming for some top schools! You're scores are some of the best in that nation.")

if compScore > 30 and compScore < 32:
	print("Wow! You're sure to get in many great colleges. ")

if compScore > 27 and compScore < 30:
	print("Great score if you're headed to a great public college!")

if compScore > 21 and compScore < 27:
	print("Your score is around the national average. Keep working and raise your score")

if compScore > 21:
	print("Your score is below the national average. Keep working and raise your score")
