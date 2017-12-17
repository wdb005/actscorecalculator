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
if compScore > 33:
    print('Wow, Enjoy MIT')
if compScore < 33 and compScore > 29:
    print('Smart kiddo aye')
if compScore > 24 and compScore < 29:
    print("Good work, you can probably get into a solid state school.")
if compScore < 24:
    print("Study and retake, you can do better")

