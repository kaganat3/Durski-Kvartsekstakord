s=str(input())
s=s.lower()
ot=0
zat=0
for slovo in s:
    if slovo=='a' or slovo=='e' or slovo=='i' or slovo=='o' or slovo=='u':
        ot+=1
    else if (slovo!=' ' or slovo!='!' or slovo!='?' or slovo!='.' or slovo!=',' or slovo!=';'):
        zat+=1

print(ot,zat)
