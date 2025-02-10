print("welcome to pizza shop :) ")
a = input("select the size of the piza s / m / l / cancel ? ")
if a == "s":
    bill = 12
    print("coxt of thr small size pizza is $12 ")
elif  a == "m":
    bill = 15 
    print("cost of the medium size pizz is $15")
elif a == "l":
    bill = 18
    print("cost of the large size pizz is $18")

else:
   print("thank you visit again ")

b = input("do you want pepperoni on your pizza? y / n ")

if b == "y":
        bill += 3
        print("after adding pepperioni your bill is = ",bill)
elif b == "n":
        print("you did not add pepperioni ")

c = input("do you want extra chess ? y / n ")
if c == "y":
        bill += 2 
        print("you total is = ",bill ) 
elif c == "n":
        print("you did not add chess")
        


tax =  bill * 10 / 100
total = tax + bill 


print("total bill = ",total )




