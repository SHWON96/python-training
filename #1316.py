N = int(input())  # 3 ccdddddbbb
list1 = [0] * N  # ['happy', 'new', 'year']
list2 = list()
count = 0  # 그룹단어가 아닌애들을 센다.

for i in range(N):
    list1[i] = input()

for i in range(N):
    b = list1[i]
    k = list(b)
    print(k)

    for j in range(len(k) - 1):
        if k[j] != k[j + 1]:
            list2.append(k[j])

        if j == (len(k) - 2) and k[j] != k[j + 1]:
            list2.append(k[j + 1])

    list1[i] = list2

    list2 = list()

print(list1)

for i in range(N):
    b = list1[i]

    for j in range(len(b)):
        for t in range(len(b)):
            if t != j and b[j] == b[t]:
                print(b)
                count = count + 1
                print(count)
                break

        else:
            continue

        break

print("answer")
print(N - count)
