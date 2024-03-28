import random
import time
import os

COUNTRIES = ["France", "Japan", "Brazil", "Canada", "Australia", "Germany", "Italy", "India", "Mexico", "Russia", "Spain", "China", "Argentina", "Egypt", "South Africa", "Greece", "Thailand", "Sweden", "Turkey", "Vietnam"]
FOOD = ["Pizza", "Sushi", "Burger", "Pasta", "Tacos", "Curry", "Salad", "Steak", "Pancakes", "Soup", "Sandwich", "Dumplings", "Sushi", "Kebab", "Omelette", "Lasagna", "Risotto", "Ramen", "BBQ"]
JOBS = ["Doctor", "Teacher", "Engineer", "Lawyer", "Nurse", "Pilot", "Chef", "Actor", "Singer", "Artist", "Firefighter", "Programmer", "Writer", "Athlete", "Astronaut", "Scientist", "Photographer", "Dentist", "Carpenter"]
SPORTS = ["Football", "Basketball", "Tennis", "Soccer", "Golf", "Swimming", "Volleyball", "Baseball", "Rugby", "Hockey", "Boxing", "Cycling", "Skiing", "Wrestling", "Athletics", "Gymnastics", "Surfing", "Cricket", "Tennis", "Badminton"]

CATEGORY = [COUNTRIES, FOOD, JOBS, SPORTS]

CATEGORY_NAMES = {
    0: "COUNTRIES",
    1: "FOOD",
    2: "JOBS",
    3: "SPORTS",
}

def hangman(attempts):
    stages = """
         ___________________
        |                   |
        |    {1}     |
        |   {0}          {2}    |
        |   {0}          {3}    |
        |   {0}         {5}{4}{6}   |
        |   {0}         {7} {8}   |
        |   X               |   
        |___________________|"""
    
    upbar = "|" if attempts < 9 else " "
    bar = "__________" if attempts < 8 else "          "
    rope = "|" if attempts < 7 else " "
    head = "O" if attempts < 6 else " "
    body = "|" if attempts < 5 else " "
    left_arm = "/" if attempts < 4 else " "
    right_arm = "\\" if attempts < 3 else " "
    left_leg = "/" if attempts < 2 else " "
    right_leg = "\\" if attempts < 1 else " "

    print(stages.format(upbar, bar, rope, head, body, left_arm, right_arm, left_leg, right_leg))


def choosing_category():
    print("We have a choice from these categories: ")
    for index, category in enumerate(CATEGORY):
        print(index + 1, ".", CATEGORY_NAMES[index])

    category = input("Choose one of these categories according to the number: ")
    while not (category.isdigit() and 1 <= int(category) <= len(CATEGORY)):
        print("This character wasn't available for selection")

        for index, category in enumerate(CATEGORY):
            print(index + 1, ".", CATEGORY_NAMES[index])

        category = input("Choose one of these categories by number: ")
    return choose_word(int(category))

def check_answer():
    answer = input("Press Y to choose from categories, for your own word, press N: ").upper().strip()
    while answer != 'Y' and answer != 'N':
        print("This character wasn't available for selection")
        answer = input("Press Y to choose from categories, for your own word, press N: ").upper().strip()
    return answer

def communication():
    print("  ____________________________\n","|Welcome to the Hangman game.|\n", "|____________________________|\n")
    print("You can choose from various categories or write a single word yourself to your friend, then the word will be erased and your friend can play. \n")

    answer = check_answer()
    
    if answer == 'Y':
        return choosing_category().upper().lstrip()

    word = input("Insert your own single-word: ").upper().lstrip()
    
    while word != word.strip() or contains_num(word):
        print("This word is not a single word")
        word = input("Try it once more: ")
    
    return word

def contains_num(word):
    for znak in word:
        if znak.isdigit():
            return True
    return False

def choose_word(category):
    words = CATEGORY[category - 1]
    return random.choice(words)

def check_difficulty():
    print("Before starting, you need to choose the difficulty: easier(1) or harder(2)")
    answer = input("Choose the difficulty level: ").upper().strip()
    
    while answer != "1" and answer != "2":
        print("This character wasn't available for selection")
        print("Before starting, you need to choose the difficulty: easier(1) or harder(2)")
        answer = input("Choose the difficulty level: ").upper().strip()
    return answer

def check_letter(letters):
    letter_input = input("Write a letter from the list: ").upper().strip()

    while letter_input not in letters:
        print("takoveto pismeno neni v seznamu")
        print_hint(letters)
        letter_input = input("Write a letter from the list: ").upper().strip()
    
    return letter_input

def type_attempts():
    print("Now we can start the game")
    answer = check_difficulty()

    attempts =  9
    if answer == "2":
        attempts = 6
    return attempts

def print_hint(letters):
    rows = [sorted(list(letters))[i:i+6] for i in range(0, len(letters), 6)]
    for row in rows:
        print(" ".join(row))

def game(word, attempts):
    letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', \
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    
    print("Let's get started with the game!")
    print("------------------------")

    word_string = ' '.join(['_' for i in range(len(word))])

    while "_" in word_string and attempts > 0:
        print()
        hangman(attempts)
        print("\n", word_string, "\n")
        print_hint(letters)
        letter_input = check_letter(letters)

        letters.remove(letter_input)

        if letter_input in word:
            for i in range(len(word)):
                if word[i] == letter_input:
                    word_string = word_string[:(i*2)] + letter_input + word_string[(i*2) + 1:]
            continue
        attempts -= 1

    hangman(attempts)
    final(attempts, word)

def final(attempts, word):
    if attempts == 0:
        print("YOU LOST! \n", "This was the sought-after word: ", word)
        return
    
    print(word, "\n" "YOU WON!")

def clear_terminal():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    word = communication()
    clear_terminal()
    attempts = type_attempts()
    game(word, attempts)

    return

if __name__ == "__main__":
    main()