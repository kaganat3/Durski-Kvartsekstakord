#Napiši program koji unosi prirodni broj i ispisuje srednju znamenku tog broja ako broj ima neparan broj znamenaka, 
#ili pak srednej dvije znamenke ako ima paran broj znamenka.
n=int(input('unesi broj'))
b=n
brojac=0
brojac2=0
while b>0:
    zz=b%10
    b=b//10
    brojac+=1
if brojac%2==0:
    while n>0:
        zz1=n%10
        n=n//10
        brojac2+=1
        if brojac2==brojac//2 or brojac2==brojac//2+1:
            print(zz1)
else:
    while n>0:
        zz1=n%10
        n=n//10
        brojac2+=1
        if brojac2==brojac//2+1:
            print(zz1)

