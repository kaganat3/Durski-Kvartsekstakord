s=str(input())
s=s.split('')
for slovo in s:
    if (slovo=='a'):
        print('b',end='')
    if (slovo=='b'):
        print('a',end='')
    else:
        print(slovo)
