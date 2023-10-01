import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def fun():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry,only letters in the alphabet please.")
        fun()
    else:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
fun()

