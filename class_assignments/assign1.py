
s = {}
while 1:
    num = int(input("Enter the number....\n"))
    if num >= 1 and num <= 9:
        s.setdefault(num, num**3)
        print(s)
    else:
        print("Invalid number...")
