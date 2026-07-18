from random import randint

def play_game(player_name, target_num, max_tries=None):
    tries = 0
    while True:
        guess = int(input(f"{player_name} - Guess Number: "))
        tries += 1

        if guess > target_num:
            print("Try Lower Number!")
        elif guess < target_num:
            print("Try Higher Number!")
        else:
            print(f"{player_name} guessed correctly in {tries} tries!")
            return tries

        # If max_tries is set (Player 2’s case), stop if exceeded
        if max_tries and tries > max_tries:
            print(f"{player_name} exceeded {max_tries} tries. Game over!")
            return None

# Player 1 plays
random_num1 = randint(0, 100)
print("Player 1, start guessing!")
p1_result = play_game("Player 1", random_num1)

# Player 2 plays with a new random number
random_num2 = randint(0, 100)
print(f"\nPlayer 2 must guess in {p1_result} tries or fewer to win!")
p2_result = 0
while True:
    guess = int(input(f"Player 2 - Guess Number: "))
    p2_result += 1

    if guess > random_num2:
        print(f"Try Lower Number! ({p1_result - p2_result} guesses left to win)")
    elif guess < random_num2:
        print(f"Try Higher Number! ({p1_result - p2_result} guesses left to win)")
    else:
        if p2_result < p1_result:
            print(f"Player 2 wins in {p2_result} tries!")
        elif p2_result == p1_result:
            print(f"It's a tie! Both guessed in {p1_result} tries.")
        else:
            print("Player 1 wins! Player 2 took too many tries.")
        break

    if p2_result > p1_result:
        print("Player 1 wins! Player 2 took too many tries.")
        break
