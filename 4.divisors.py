num = int(input("Enter a number: "))
for i in range(1, num):
    if num % i == 0:
        print(i)
print([x for x in range(1, num) if num % x == 0])
