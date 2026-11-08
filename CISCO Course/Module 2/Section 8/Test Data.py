def read_int(prompt, min, max):
    while True:
        value = input(prompt)
        try:
            number = int(value)
        except ValueError:
            print("Error: wrong input")
            continue
        if number < min or number > max:
            print("Error: the value is not within permitted range (-10..10)")
        else:
            return number
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
