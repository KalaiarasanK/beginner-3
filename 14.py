A=int(input())
B=str(input())
B=list(B)
for i in B:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		B.remove(i)
C=B[::-1]
print("".join(C))
