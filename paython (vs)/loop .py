n = int(input("enter your first number = "))
a = int(input("enter your last number = "))
n = 0 
while n <= a:
    n += 1
    if n /2 == 0:
        print(n,"number is even")
    else:
        print(n,"number is odd ")
