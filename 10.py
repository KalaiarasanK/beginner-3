A,B=list(map(str,input().split()))
C=0
for i in range (0,len(A)):
	if A[i]!=B[i]:
		C+=1
if(C==1):
	print("Yes")
else:
	print("No")
