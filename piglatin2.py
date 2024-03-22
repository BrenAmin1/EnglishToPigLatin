########################
#Pig Latin from English#
########################
#!/usr/bin/env python3
import string

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def turnFileIntoList(text):
	tempList = []
	temp = ""
	F = open(text, "r")
	for x in F:
		tempList += x	
	F.close()
	finalList = []
	for x in tempList:
		if not x.isspace():
			temp += x
			#print(temp)
		if x.isspace():
			finalList.append(temp)
			temp = x
			finalList.append(temp)
			temp = ""
		
	return finalList

def turnListIntoPigLatin(myList):
	for word in myList:
		if not word.isspace() and "\n" in word:
			#tempChar = word[0]
 			#print(tempChar)
 			print(word)
	finalList = []
	for word in myList:
		finalList.append(word)
	return finalList

def main():
	myList = turnFileIntoList("data.txt")
	turnListIntoPigLatin(myList)
	#print(turnListIntoPigLatin(myList))
	#print(myList)
	#turnFileIntoList("data.txt")

if __name__ == "__main__":
	main()
	
	
"""
if word[0] in vowels:
				word += "way"
				continue
			elif word[0] in consonants and word[1] in vowels:
				tempWord = word[0]
				word = word[1:]
				word += tempWord + "ay"
				continue
			elif word[0] in consonants and word[1] in consonants:
				tempWord = word[0] + word[1]
				word = word[2:]
				word += tempWord + "ay"
				continue
"""	
	



