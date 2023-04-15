a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a == b == c:
    print("Triangle is equilateral")
elif a == b or b == c or c == a:
    print("Triangle is isosceles")
else:
    print("Triangle is right angle trangle")