s=str(input())
s=s.split('.')
print(s[0],end='.')
s=s[1]
s=s.split(' ')
if (s[0]=='siječanj'):
    print("01.",end='')
if (s[0]=='veljača'):
    print("02.",end='')
if (s[0]=='ožujak'):
    print("03.",end='')
if (s[0]=='travanj'):
    print("04.",end='')
if (s[0]=='svibanj'):
    print("05.",end='')
if (s[0]=='lipanj'):
    print("06.",end='')
if (s[0]=='srpanj'):
    print("07.",end='')
if (s[0]=='kolovoz'):
    print("08.",end='')
if (s[0]=='rujan'):
    print("09.",end='')
if (s[0]=='listopad'):
    print("10.",end='')
if (s[0]=='studeni'):
    print("11.",end='')
if (s[0]=='prosinac'):
    print("12.",end='')
print(s[1]+'.')
