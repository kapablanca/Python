import tkinter as tk
import pandas as pd
import random

index = 0

for _ in range (4):
    languages = ["French", "English"]
    df = pd.read_csv("./data/french_words.csv")

    language = languages[index]

    word = df[language].sample().values[0]

    print(word)

    word = df[df["French"] == word].values[0][1]

    print(word)
    index = (index +1) % len(languages)

