a=input("Enter your name: ")
b=int(input("Enter your age: "))
c=float(input("Enter your annual salary: "))
if b>18 and c>21000:
    print("congratulations",a,"you qualify to apply for the loan")
    if c>21000 and c<=30000:
        print("Your limit is 20000")
        d=float(input("Enter the amount you wish to borrow: "))
        if d<=20000:
            print("Your loan is being processed now ,you will be notified through your email when ready ")
        else:
            print("SORRY!You can only borrow up to 20000, please try again ")
    elif c>30000 and c<=40000:
        print("Your limit is 30000")
        e=float(input("Enter amount you wish to borrow: "))
        if e<=30000:
            print("Your loan is being processed now ,you will be notified through your email when ready ")
        else:
            print("SORRY!You can only borrow up to 30000, please try again ")
    elif c>40000 and c<=50000:
        print("Your limit is 40000")
        f=float(input("Enter amount you wish to borrow: "))
        if f<=40000:
            print("Your loan is being processed now ,you will be notified through your email when ready ")
        else:
            print("SORRY!You can only borrow up to 40000, please try again ")
    elif c>50000 and c<=100000:
        print("Your limit is 50000")
        g=float(input("Enter amount you wish to borrow: "))
        if g<=50000:
            print("Your loan is being processed now ,you will be notified through your email when ready ")
        else:
            print("SORRY!You can only borrow up to 50000, please try again ")
    elif c>100000:
        print("Your limit is 100000")
        h=float(input("Enter amount you wish to borrow: "))
        if h<=100000:
            print("Your loan is being processed now ,you will be notified through your email when ready ")
        else:
            print("SORRY!You can only borrow up to 100000, please try again ")
    else:
        print("Please enter valid amount ")
else:
    print("Sorry",a,"you do not qualify to apply for a loan")