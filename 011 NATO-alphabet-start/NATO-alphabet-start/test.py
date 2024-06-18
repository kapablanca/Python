import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")


nato = {row.letter: row.code for (index, row) in df.iterrows()}

print(nato["A"])