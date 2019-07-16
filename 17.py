A1,A2=map(int,input().split())
num=1
while num>0:
	if num%A1==0 and num%A2==0:
		print(num)
		num=0
	else:
		num+=1
