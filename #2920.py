A=input()
list1=A.split(" ")
print(list1)
ascending=['1','2','3','4','5','6','7','8']
descending=['8','7','6','5','4','3','2','1']

if list1==ascending:
    print('ascending')
elif list1==descending:
    print('descending')
else:
    print('mixed')

