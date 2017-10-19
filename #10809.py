S=input()
k=list(S)
print(k)
Alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(Alph)

for j in range(len(Alph)):
    for i in range(len(k)):
        if k[i]==Alph[j]:
            print(i,end=" ")
            break
        elif k[i]==k[-1] and i==len(k)-1:
            print(-1,end=" ")

