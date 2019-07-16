num=int(input())
alpha=sorted("kabali")
count=0
for i in range(num):
	Name=input("")
	A=sorted(Name)
	if alpha==A:
		count+=1
print(count)
