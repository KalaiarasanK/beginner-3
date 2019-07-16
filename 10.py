A,B=list(map(str,input().split()))
c=0
for i in range (0,len(A)):
	if A[i]!=B[i]:
		c+=1
if(c==1):
	print("Yes")
else:
	print("No")
