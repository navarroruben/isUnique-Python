# Ruben Navarro
# 11/27/2019
# CTCI - isUnique - Python edition
# Determines if a string has all unique characters

words = ["abcde", "hello", "apple", "kite", "padle"]

for word in words:
    w = sorted(word)
    ws = set(w)

    if (len(word) != len(ws)):
        print("{:s} does NOT contain Unique characters".format(word))
    else:
        print("{:s} contains Unqiue characters".format(word))