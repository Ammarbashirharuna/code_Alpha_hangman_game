import random
from words import words


hang_man = {0:(" ",
          " ",
          " "),
        1:(" o ",
            " ",
            " "),
        2:("  o ",
           "  | "
            " "),
        3:(  " o ",
             "/| ",
              " "),
         4:( "  o   ",
             " /|\\ ",
              "  "),
          5:("  o   ",
             " /|\\ ",
             " /    "),
          6:(  "  o ",
               " /|\\ ",
               " / \\")

 }

def display_man(wrong_guesses):
    print("**********************")
    for line in hang_man[wrong_guesses]:
        print(line)
    print("**********************")



def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        Guess = input("Enter a later ")

        if len(Guess) != 1 or not Guess.isalpha():
            print("invalid input")
            continue

        if Guess in guessed:
            print(f"{Guess} is already Guess")
            continue

        if Guess in answer:
            for i in range(len(answer)):
                if answer[i] == Guess:
                    hint[i] = Guess

        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            hang_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False

        elif wrong_guesses >= len(hang_man) - 1 :
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running = False





if __name__ == "__main__":
    main()
