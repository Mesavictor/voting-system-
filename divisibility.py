a=int(input("Enter a number "))
b=a%5
c=a%2
d=a%11
if b==0:
    print(a,"is divisible by 5")
else:
    print(a,"is not divisible by 5")
if c==0:
    print(a,"is an even number ")
else:
    print(a,"is not an even number ")
if d==0:
    print(a,"is divisible by 11")
else:
    print(a,"is not divisible by 11")