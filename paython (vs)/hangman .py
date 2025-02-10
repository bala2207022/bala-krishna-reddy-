import random 

stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    GAME OVER!
    """
]

a = ["great", "grate", "heart", "earth", "stare", "tears", "stone", "tones", "brake", "break", "angel", "angle"]
lives = 6

selectedword = random.choice(a)

hidden_word = "*" * len(selectedword)
print("Selected word: " + hidden_word) 

x = "_" * len(selectedword)  
print(x)
word = len(selectedword)

game_over = False
correct_letter = []

while not game_over:
    b = input("guess a letter = ").lower()
    display = ""

    for letter in selectedword:
        if letter == b:
            display += letter 
            if letter not in correct_letter:  
                correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter 
        else:
            display += "_"

    print(display)

    if b not in selectedword:
        lives -= 1
        if lives == 0: 
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[6 - lives])
