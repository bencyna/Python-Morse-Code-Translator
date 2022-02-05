import pandas
import os

codes = pandas.read_csv("morser_codes.csv")

go_on = True
while go_on:
    try:
        choice = input("Translate to or from mores code? Enter the related number\n1. English->morse cdode\n" \
                       "2. More code into english\nType exit to leave the application\n")
        if choice == "1":
            codes_dict = {row.letter: row.code for (index, row) in codes.iterrows()}

            to_decode = input("What do you want to encode\n").upper()
            array_to_decode = [codes_dict[letter] for letter in to_decode]
            print("Your morse code: \n" + " ".join(array_to_decode))

        elif choice == "2":
            codes_dict = {row.code: row.letter for (index, row) in codes.iterrows()}
            to_decode = input("What do you want to encode\n").upper()
            decode_arr = to_decode.split(" ")
            array_to_decode = [codes_dict[letter] for letter in decode_arr]

            print("Your decoded letters: \n" + " ".join(array_to_decode))

        elif choice == "exit":
            print("Goodbye")
            go_on = False
        else:
            print("Invalid please try again")

        input("Press enter to go again")

    except KeyError:
        print("There was a spacing or letter issue, try again :)")

    cls = lambda: os.system('cls')
    cls()
