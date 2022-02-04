import pandas

codes = pandas.read_csv("morser_codes.csv")

codes_dict = {row.letter: row.code for (index, row) in codes.iterrows()}
print(codes_dict)

go_on = True
while go_on:
    choice = input("Translate to or from mores code? Enter the related number\n1. English->morse cdode\n"\
          "2. More code into english\n")
    if choice == "1":
        to_decode = input("What do you want to encode\n").upper()
        array_to_decode = [codes_dict[letter] for letter in to_decode ]
        print(" ".join(array_to_decode))

    elif choice == "2":
        print("Morse to english")
    else:
        print("Invalid please try again")
    break