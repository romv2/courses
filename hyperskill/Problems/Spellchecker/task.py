dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]


def spellchecker():
    print('Correct' if input() in dictionary else 'Incorrect')


spellchecker()
