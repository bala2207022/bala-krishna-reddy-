print("Welcome to the Island Game!")

choice = input("Select 'right' or 'left': ").lower()

if choice == "left":
    print("You're safe! Go slow.")
    b = input("Water is ahead. Do you want to 'swim' or 'wait' for a boat? ").lower()

    if b == "wait":
        print("Please wait till the boat arrives...")
        c = input("You crossed the water! Do you want to 'climb' or use a 'rope'? ").lower()

        if c == "climb":
            print("🏆✨💰 Congratulations! You found the hidden treasure! 💰✨🏆")
        
        else:
            print("You don't have a rope! Game Over. ❌")

    else:
        print("You can't swim! There are wild animals inside the water. 🐊🐍 Game Over. ❌")

else:
    print("You fell into a hole! 🕳️ Game Over. ❌")
