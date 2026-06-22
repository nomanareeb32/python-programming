a = "Life is painful"
print("Is life hard?") ; print("Please answer with Yes or No")
b = input(str())
if b == "Yes":
	print(a)
elif b == "No":
	print(a.replace("is", "isn't"))
else:
	print("You are fucked up")
