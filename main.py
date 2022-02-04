import pandas

codes = pandas.read_csv("morser_codes.csv")

codes_dict = {row.letter: row.code for (index, row) in codes.iterrows()}

go_on = True
while go_on:
    choice = input("Translate to or from mores code? Enter the related number\n1. English->morse cdode\n"\
          "2. More code into english\n")
    if choice == "1":
        print("English to morse")
    elif choice == "2":
        print("Morse to english")
    else:
        print("Invalid please try again")
    break