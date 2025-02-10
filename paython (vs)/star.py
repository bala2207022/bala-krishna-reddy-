rows = 5
i = 1


while i <= rows:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i += 1

i = rows - 1
while i > 0:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i -= 1





print (selectedword)
b = input("guess a letter = ").lower()
print(b)
for letter in selectedword:
    if letter == b:
        print ('right')
    else:
        print('wrong')