A=int(input())
B=list(map(int,input().split()))
C=1
for i in B:
	if B.count(i)==C:
		S1=i
print(S1)
