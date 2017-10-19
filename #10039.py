A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
sum=0
list1=[A,B,C,D,E]
for i in range(len(list1)):
    if list1[i] <= 40:
        list1[i]=40
    sum=sum+list1[i]

print(int(sum/5))

