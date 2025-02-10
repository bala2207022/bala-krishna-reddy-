import random

print("🎮 Welcome to the Randomized Adventure Game! 🎮")

choice = input("Do you want to go 'left' or 'right'? ").lower()


events = ["treasure", "enemy", "trap", "potion"]
event = random.choice(events)  

print(f"You chose {choice} and encountered a {event}! 🚀")

if event == "treasure":
    gold = random.randint(50, 500) 
    print(f"🎉 You found a hidden treasure with {gold} gold coins! 💰")

elif event == "enemy":
    print("⚔️ An enemy appears! You must roll a dice to fight.")
    player_roll = random.randint(1, 6) 
    enemy_roll = random.randint(1, 6)   
    print(f"You rolled: {player_roll} 🎲 | Enemy rolled: {enemy_roll} 🎲")

    if player_roll > enemy_roll:
        print("🏆 You defeated the enemy! Victory!")
    else:
        print("💀 You lost the fight and had to run away!")

elif event == "trap":
    damage = random.randint(10, 50)  
    print(f"😱 You fell into a trap and lost {damage} HP!")

elif event == "potion":
    health = random.randint(20, 100)  
    print(f"🧪 You found a magical potion and regained {health} HP!")

print("🎮 Game Over! Thanks for playing. 🚀")
