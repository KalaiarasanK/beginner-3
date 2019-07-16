d1=int(input())
Sum=0
dig=0
while(d1>0):
	dig=d1%10
	Sum+=dig*dig
	d1=d1//10
print(Sum)	
