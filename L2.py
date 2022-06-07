s=str(input())
s=s.split(' ')
def f(s):
    return len(s)
l=s
l.sort(key=f)
print(l[0], len(l[0]) )
print(l[-1],len(l[-1]) )
print(s.index(l[0]))
print(s.index(l[-1]))
