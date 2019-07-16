S1,S2=list(map(str,input().split()))
c=0
for i in range (0,len(S1)):
	if S1[i]!=S2[i]:
		c+=1
if(c==1):
	print("yes")
else:
	print("no")
