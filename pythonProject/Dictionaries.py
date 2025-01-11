# example_1 = {1: 123, 2: 234, 3: 345, 4: 456, 5: 567}
# print(example_1[3])
# print(2 in example_1)
# print(6 not in example_1)

# exp_2 = {"Queen": "Bohemian Rhapsody",
#          "Bee Gees": "Stayin' Alive",
#          "U2": "One",
#          "Michael Jackson": "Billie Jean",
#          "The Beatles": "Hey Jude",
#          "Bob Dylan": "Like A Rolling Stone"}
#
# print(len(exp_2))
#
# for key in exp_2.keys():
#     print(key)
#
# print(exp_2.values())
#
# for key, value in exp_2.items():
#     print(key, value)
#
# print(exp_2.get("Promise of the Real", "That is not a key that appears in the dictionary."))

# exp_3 = {"b": "consonant",
#          "c": "consonant",
#          "d": "consonant",
#          "f": "consonant",
#          "g": "consonant",
#          "h": "consonant",
#          "j": "consonant",
#          "k": "consonant",
#          "l": "consonant",
#          "m": "consonant",
#          "n": "consonant",
#          "p": "consonant",
#          "q": "consonant",
#          "r": "consonant",
#          "s": "consonant",
#          "t": "consonant",
#          "v": "consonant",
#          "w": "consonant",
#          "x": "consonant",
#          "y": "consonant",
#          "z": "consonant"}
#
# for key, value in exp_3.items():
#     print(key, value)
#
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}

# p = fast_food_items.pop("McDonald's")
# print(fast_food_items)
# print(p)

# fast_food_items.popitem()
# print(fast_food_items)

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)
ab = internet_celebrities.copy()
print(ab)
internet_celebrities.clear()
print(internet_celebrities)




