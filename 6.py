A=list(input(""))
for i in range(0,len(A),2):
	B="".join(A[i+1]+A[i])
	print(B,end='')
