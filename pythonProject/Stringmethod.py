mixed_case = "A Song Of Ice And Water"

# print(mixed_case.isupper())
# print(mixed_case.islower())

# print(mixed_case.upper())
# print(mixed_case.lower())
print(mixed_case.istitle())
print(mixed_case.title())
#
# title_case = mixed_case.title()
# # print(title_case)
print(mixed_case.startswith("A"))
# print(mixed_case.endswith("e"))
# words = mixed_case.split()
# print(words)
#
# print(" ".join(words).isalpha())

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, '*'))
# center_plus = the_string.center(16, '+')
# # print(center_plus)
# # print(the_string.lstrip("North"))
# print(center_plus.strip("+"))
# print(the_string.replace("North", "South"))

# def reverse_string(string):
#     rev = ""
#     for i in range(len(reverse)-1, -1, -1):
#         rev += reverse[i]
#     return rev
#
#
# reverse = input("Enter the string:")
# print(reverse_string(reverse))

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."


# def word_counter(words):
#     spaces_and_letters = ""
#     word_count = 1
#     for i in words:
#         if i.isalnum() or i.isspace() or i == "-" or i == "'":
#             spaces_and_letters += i
#     for j in spaces_and_letters:
#         if j == " ":
#             word_count += 1
#     return word_count
#
#
# print(word_counter(str_1))
# print(word_counter(str_2))
# print(word_counter(str_3))

def word_count(words):
    wording = ""
    word_counting = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            wording += i
    for j in wording:
        if j == " ":
            word_counting += 1
    return word_counting


string = input("Enter the string:")
print(word_count(string))
