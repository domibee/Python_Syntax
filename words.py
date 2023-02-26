def print_upper_words(words):
    for word in words:
        print(word.upper())

print_upper_words(["Programming", "is","pretty","fun"])

def words_with_e(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

words_with_e(["Edward"])

def specify_words(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word)
                break

specify_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

specify_words(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])