lst = ["apple", "banana", "kiwi", "strawberry", "fig"]
vowels = "aeiouAEIOU"
count = 0

for i in lst:
    if i[0] in vowels:
        count += 1

print(count)

"""
lst = ["apple", "ebanana", "ikiwi", "strawberry", "fig"]
# vowels = "aeiouAEIOU"
count = 0

for word in lst:
    if word.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
        count += 1

print(count)
"""