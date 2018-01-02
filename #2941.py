# c= , c- , dz= , d- , lj , nj , s= , z=   총 8개

N = input()
list1 = list()  # =받는애
list2 = list()  # -받는애
list3 = list()  # j 받는애
count = 0
# print(len(N))

for i in range(len(N)):
    if N[i] == '=':
        list1.append(i)

for i in range(len(N)):
    if N[i] == '-':
        list2.append(i)

for i in range(len(N)):
    if N[i] == 'j':
        list3.append(i)

# print(len(list1))
# print(len(list2))
# print(len(list3))


for i in range(len(list1)):

    if N[list1[i] - 1] == 'c':
        count = count + 1
    elif N[list1[i] - 1] == 's':
        count = count + 1
    elif N[list1[i] - 1] == 'z':
        if list1[i] >= 2 and N[list1[i] - 2] == 'd':
            count = count + 2
        else:
            count = count + 1

# print(count)

for i in range(len(list2)):

    if N[list2[i] - 1] == 'c':
        count = count + 1
    if N[list2[i] - 1] == 'd':
        count = count + 1

# print(count)

for i in range(len(list3)):

    if N[list3[i] - 1] == 'l':
        count = count + 1
    if N[list3[i] - 1] == 'n':
        count = count + 1
# print(count)

print(len(N) - count)