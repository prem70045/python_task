a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a == b or b == c or c == a:
    print("Sum is zero")
else:
    sum = a + b + c
    print("Sum is", sum)
