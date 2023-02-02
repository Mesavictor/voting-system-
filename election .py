country=["kenya","tanzania","uganda"]
name=["joseph","dan","lucy"]
a=input("Enter the name of your country: ").lower()
b=int(input("Enter your age: "))
if (a in country) and b>18:
    print("You qualify to vote ")
    print("Below is the   list of candidates: ")
    print("1.Joseph")
    print("2.Dan")
    print("3.Lucy")
    c=input("TO VOTE, enter the name of your preferred candidate: ").lower()
    if (c in name):
        print("Thank you for your vote ")
    else:
        print("INVALID CANDIDATE!Please choose one candidate from the names displayed above ")
else:
    print("You do not qualify to vote ")