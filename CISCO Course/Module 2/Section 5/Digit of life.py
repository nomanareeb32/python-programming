date = input("Enter your birthday (YYYYMMDD): ")
total = 0
for ch in date:
    total = total + int(ch)
while total >= 10:
    new_total = 0
    for ch in str(total):
        new_total = new_total + int(ch)
    total = new_total
print("Your Digit of Life is:", total)