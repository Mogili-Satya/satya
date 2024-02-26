n=int(input("enter the no.of students"))
x=int(input("no.of chocolates available"))
if n>= x:
    np=0
else:
    a=n-x
    if a%4==0:
        np=a//4
    else:
        np=(a//4)+1
print(np)
