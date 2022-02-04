import pandas

codes = pandas.read_csv("morser_codes.csv")

codes_dict = {row.letter: row.code for (index, row) in codes.iterrows()}
print(codes_dict)
