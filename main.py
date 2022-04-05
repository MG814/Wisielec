import sys
import re
import json
import random

user_word = []
user_letters = []
again = "0"
chan = 0

with open("words.json") as json_file:
    words = json.load(json_file)

i = random.randint(0, 14)
word = words[i]["json_word"]


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


def reset():
    user_word.clear()
    user_letters.clear()
    for _ in word:
        user_word.append("_")


reset()

while True:

    while True:
        print("\nPoziom trudności.")
        print("0 - Wyjście \n1 - Łatwy (5 szans) \n2 - Średni (3 szanse) \n3 - Trudny (1 szansa)")
        choice = input("Wybierz opcje: ")
        if choice == "1":
            chan = 5
            print("\nWybrano poziom łatwy.")
            break
        if choice == "2":
            chan = 3
            print("\nWybrano poziom średni.")
            break
        if choice == "3":
            chan = 1
            print("\nWybrano poziom trudny.")
            break
        if choice == "0":
            if chan == 0:
                print("\nNajpierw wybierz poziom trudności.")
            else:
                break

    menu = input("\nWciśnij 1 aby rozpocząc grę: ")

    if menu == "1" or again == "1":

        chances = chan

        while True:

            letter = input("\nPodaj literę: ")

            while not bool(re.match(r"^([a-z])$", letter)):
                print("Nie poprawnie.")
                letter = input("Podaj literę jeszcze raz: ")

            while letter in user_letters:
                print("\nPodano już taką literę.\n")
                letter = input("Podaj inną literę: ")

            user_letters.append(letter)

            found_indexes = find_indexes(word, letter)

            if len(found_indexes) == 0:
                print("Nie ma takiej litery.")
                chances = chances - 1
                if chances == 0:
                    print("Przegrałeś.\nSzukane słowo to:", word)
                    again = input("Chcesz zagrać jeszcze raz? \n 1 - TAK \n 2 - NIE\n")
                    reset()
                    if again == "1":
                        chances = chan
                    if again == "2":
                        sys.exit(0)
            else:
                for index in found_indexes:
                    user_word[index] = letter
                    if "".join(user_word) == word:
                        print("Wygrałeś!\nSzukane słowo to:", word)
                        again = input("Chcesz zagrać jeszcze raz? \n 1 - TAK \n 2 - NIE\n")
                        reset()
                        if again == "1":
                            chances = chan
                        if again == "2":
                            sys.exit(0)

            print("Pozostało", chances, "szans")
            print("".join(user_word))
            print("Użyte litery: ", user_letters)