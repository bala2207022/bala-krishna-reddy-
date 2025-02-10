print("Welcome to the Ride!")

height = float(input("Enter your height in feet: "))
age = int(input("Enter your age: "))


if height > 5.6:
    print("You're good to take the ride!")

 
    if 45 < age <= 55:
        print("Warning: It's dangerous for people aged 45 to 55 due to the ride's fast movements.")
        proceed = input("Do you still want to proceed? Type 'y' for yes or 'n' for no: ").lower()
        if proceed == "n":
            print("Thank you for your caution. You can exit the queue.")
        else:
            
            bill = 20  
            print("Adult ticket is $20.")
    else:
        
        if age <= 10:
            bill = 15
            print("Child ticket is $15.")
        elif age <= 18:
            bill = 18
            print("Youth ticket is $18.")
        else:
            bill = 20
            print("Adult ticket is $20.")

   
    if 'bill' in locals():  
        picture_option = input("Do you want a picture while riding? Type 'y' for yes or 'n' for no: ").lower()
        if picture_option == "y":
            bill += 3
            print("Picture added for $3.")

        
        print(f"Your total bill for the ride is: ${bill}")
else:
    print("Sorry, you can't get on the ride due to height restrictions.")
