import random

b = input("select one from 'rock' 'paper' or 'scissior'? ").lower()
a = ("rock","paper","scissior")
event = random.choice(a)
print(f"You chose {b} and encountered a {event}!")
if b not in a:
    print(" Invalid choice! Please restart and enter 'rock', 'paper', or 'scissors'.")
elif b == event:
    print("🤝 It's a tie!")
elif (b == "rock" and event == "scissors") or \
     (b == "scissors" and event == "paper") or \
     (b == "paper" and event == "rock"):
    print("🎉 You win! ")
else:
    print(" You lose! The computer wins. ")

