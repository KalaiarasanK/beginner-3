char=list(input())
last=[]
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in char:
	if i=='X':
		last.append("A")
	elif i=='Y':
		last.append("B")
	elif i=="Z":
		last.append("C")
	else:
		last.append(letter[letter.index(i)+3])

print("".join(last))	
		
