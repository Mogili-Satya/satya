a,b=map(float,input().split(" "))
if a>b:
    print("insufficient amount")
else: 
    if a<b and x%5==0:
        print("transaction is successful")
    else:
        print("incorrect with draw amount(not multiple of 5)")
