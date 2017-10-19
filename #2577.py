
A=int(input())
B=int(input())
C=int(input())

d=str(A*B*C)    # 곱한 값을 문자로 전환
N=list(d)       # 문자로 전환한것을 배열로 전환
print(N)

for i in range(10): #숫자는 0~9개로 총 10개니깐
    e=0
    for j in range (len(N)):
        if i==int(N[j]):
            e=e+1
    print('숫자 {}는 {}개 입니다.'.format(i,e))
    #print(e)

# 지철오빠 코딩
"""
A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)
print(total)
result = [0]*10

for ch in total:
    result[int(ch)] += 1

for i in result:
    print(i)
"""