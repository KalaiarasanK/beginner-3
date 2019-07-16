A,B=map(int,input().split())
C=list(map(int,input().split()[:A]))
for i in range (0,B):
	C=[C[-1]]+C[:-1]
for j in C:
	print(j,end=" ")
