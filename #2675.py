def printT():
    R = int(input())
    S=input()
    k=list(S)
    e=[i for i in range(len(k))]
    for i in range(len(k)):
        e[i]=k[i]*R
        print(e[i],end="")


T = int(input())
for i in range(T):
    printT()
