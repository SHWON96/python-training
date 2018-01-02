input1=input().split(" ")
A = input1[0]
B = input1[1]
list1=[0]*len(A)
list2=[0]*len(B)
for i in range(len(A)):
    list1[len(A)-i-1]=A[i]

for i in range(len(B)):
    list2[len(B)-i-1]=B[i]

D = int(''.join(list2))
C = int(''.join(list1))

if C > D:
    print(C)
else:
    print(D)

