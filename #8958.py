s=int(input()) # 입력한 문제의 수
t=[i for i in range(s)] # 문제 OX 받는거

def score():
    for k in range(len(t)):
        t[k]=input().upper()
        Test=list(t[k])
        e=[j for j in range(len(Test))]     # 점수 넣는 변수
        O='O'
        X='X'
        for i in range(len(Test)):
            if Test[i]==O:
                if 0<i and i<(len(Test)):
                    if Test[i-1]==O and Test[i]==O :
                        e[i]=e[i-1]+1
                    else:
                        e[i]=1
                else:
                    e[i]=1
            else:
                e[i]=0

        #print(e)
        sum=0

        for i in range(len(e)):
            sum = sum + e[i]
        print(sum)

score()

#  지철오빠 코딩
"""   
num = int(input())

while num > 0:
    num -= 1
    in_str = input()
    score = 0  # output result
    stacked = 0
    for ch in in_str:
        if ch == 'O':
            score += 1+stacked
            stacked += 1
        else:
            stacked = 0

    print(score)
"""