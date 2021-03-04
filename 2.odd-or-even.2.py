num = input("Enter a number: ")
check = input("Enter a check number: ")
if int(num) % int(check) == 0:
    print("The number is a multiple of the check number")
else:
    print("The number is a not multiple of the check number")
