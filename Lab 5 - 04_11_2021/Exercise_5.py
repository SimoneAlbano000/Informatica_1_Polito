# The code will classify french words

exceptions = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaire", "Zimbabwe"]
plurals = ["Etats-Unis", "ays-Bas"]

word = input("Type the name of a french country... ")

if word not in exceptions and word not in plurals and word[-1] == "e":
    new_word = "la " + word
    print(new_word)
elif word not in exceptions and word not in plurals and word[-1] != "e":
    new_word = "le " + word
    print(new_word)
elif word not in exceptions and word not in plurals and word[0] in "aeiou":
    new_word = "l' " + word
    print(new_word)
elif word in exceptions:
    new_word = "le " + word
    print(new_word)
elif word in plurals:
    new_word = "les " + word
    print(new_word)



