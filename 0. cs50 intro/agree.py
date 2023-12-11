s = input("do you agree? ")

s = s.lower()
if s in ["y" , "yes"]:
    print("agreed")
elif s in ["N", "no"]:
    print("not agreed")