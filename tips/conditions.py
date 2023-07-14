name = "Peter"
if name == "Adam" or name == "Peter" or name == "Jack":
    print(name)

if name in ("Adam", "Peter", "Jack"):
    print(name)

a = b = c = d = None
a = b = c = d = True
if a and b and c and d:
    print ("All True")

if all((a, b, c, d)): print("All True")
if any((a, b, c, d)): print("Any True")
