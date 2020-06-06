isPal = input("What is your potential Palidrome?\n")
isPalList = list(isPal)
flag = True

for i in range (0,len(isPalList)):
	if isPalList[i] != isPalList[len(isPalList)-i-1]:
		flag = False
		break

if flag == True:
	print(isPal + " is a Palidrome")
else:
	print(isPal + " is not a Palindrome")
