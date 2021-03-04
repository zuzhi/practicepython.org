a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 98]

print(a)
num = int(input("Enter a number: "))
print([x for x in a if x < num])

