print("welcome to fizzbuzz game ")
ready = input("want to play game y/n ").lower()
if ready == "y": 
 for num in range(1,101) :
    if num % 3 == 0 and num % 5 == 0 :
        print("fizzbuzz")
    elif num % 3 == 0 :
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
 else:
    print("thank you")       