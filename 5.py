num1,num2=map(str,input().split())
for i in num1:
	A=num1.count(i)
for j in num2:
	B=num2.count(j)
if(A==B):
	print("yes")
else:
	print("No")
