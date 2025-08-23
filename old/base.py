import random


def play_game():
    numero = random.randint(1, 10)
    arvaukset = []  # näyttää aikasemman kierroksen yritykset
    print(
        "\nUusi kierros alotettu!               by:kiiiuli \ntätä ei vissii pysty clearaa\n"
    )
    while True:
        try:
            arvus = int(
                input("arvaa numero 1-10: ")
            )  # guess on pelaajan arvaama numero
        except ValueError:
            print("ooks vittu dena?")
            continue

        arvaukset.append(arvus)

        if arvus == numero:
            print("🎉 Gz @@@@@@@!")
            print(f"arvasit täl kierrokssel: {arvaukset}\n")
            break
        elif arvus < numero:
            print("💀 liia pieni, yritä uusiks\n")
        else:
            print("💀 liia iso, yritä uusiks\n")


if __name__ == "__main__":
    while True:
        play_game()
        replay = input("pelaa uusiks? (y/n): ").strip().lower()
        if replay != "y":
            print("kiitti vitust pelaamisest!")
            break
