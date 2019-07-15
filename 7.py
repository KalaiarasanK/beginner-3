roman=('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX')
int=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
K=str(input())
for i in range(20):
	if (K==roman[i]):
	    print(int[i])
	    break
