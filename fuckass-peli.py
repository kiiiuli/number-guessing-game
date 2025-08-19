import random


def play_game():
    number = random.randint(1, 10)
    guesses = []  # alottaa uude lista joka runi
    print("\nUusi kierros alotettu! \nEn tiiä mite tä history pystyy clearaa lol\n")
    while True:
        try:
            guess = int(input("arvaa numero 1-10: "))
        except ValueError:
            print("ooks vittu dena?")
            continue

        guesses.append(guess)

        if guess == number:
            print("🎉 Gz @@@@@@@!")
            print(f"arvasit täl kierrokssel: {guesses}\n")
            break
        elif guess < number:
            print("💀 liia pieni, yritä uusiks\n")
        else:
            print("💀 liia iso, yritä uusiks\n")


if __name__ == "__main__":
    while True:
        play_game()  # alottaa pelin uudelleen
        replay = input("pelaa uusiks? (y/n): ").strip().lower()
        if replay != "y":
            print("kiitti vitust pelaamisest!")
            break
