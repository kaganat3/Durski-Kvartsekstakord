while True:
    s=str(input())
    if (s=="KRAJ"):
        break
    s=s.split(' ')
    print(s[1], s[0][0]+'.')
