lst = ["apple", "banana", "kiwi", "strawberry", "fig"]
longest = ""
for s in lst:
    if len(s) > len(longest):
        longest = s
print(longest)

"""
lst = ["apple", "banana", "kiwi", "strawberry", "fig"]
longest = max(lst, key=len) #max is the built-in function and it loops through lst with the key of checking = length
print(longest)
"""