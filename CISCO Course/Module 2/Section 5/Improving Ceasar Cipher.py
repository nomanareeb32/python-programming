text = input("Enter your message: ")
key = int(input("Enter your key: "))
cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char
        continue

    if char.isupper():
        base = ord('A')
    else:
        base = ord('a')

    shifted = (ord(char) - base + key) % 26
    cipher += chr(base + shifted)

print(cipher)