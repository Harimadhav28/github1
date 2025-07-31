import random

def snake_and_ladder():
    snakes = {25: 10, 40: 5, 90: 48}
    ladders = {3: 22, 50: 75, 70: 89}
    position = 0

    print("Starting the game of Snake and Ladder!")
    print(f"Snakes: {snakes}")
    print(f"Ladders: {ladders}")

    while position < 100:
        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print(f"\nYou rolled: {dice}")

        if position + dice > 100:
            print(f"Cannot move. Current Position: {position}")
            continue

        position += dice
        print(f"Moved to {position}")

        # Check for snakes or ladders
        if position in snakes:
            print(f"Oops! Snake bite at {position}. Sliding down to {snakes[position]}")
            position = snakes[position]
        elif position in ladders:
            print(f"Yay! Ladder at {position}. Climbing up to {ladders[position]}")
            position = ladders[position]

        print(f"Current Position: {position}\n")

    print("\nCongratulations! You reached position 100 and won the game!")

snake_and_ladder()
