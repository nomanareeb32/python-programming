numbers = input().split("+")
numbers.sort()
output = ""
for number in numbers:
    output = output + number + "+"
print(output[:-1])
