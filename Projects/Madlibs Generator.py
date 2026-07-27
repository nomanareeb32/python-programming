with open("Madlibs Story.txt", "r") as f:
    story = f.read()

words = set() #to store the words that need to be replaced
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i #7

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] #<adjective1>
        words.add(word)
        start_of_word = -1

answers = {} #dictionary to store the answers

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

# In the <adjective1> land of <place>, a <animal> was feeling <emotion>. The <animal> had lost its <object>.

# Suddenly, a <character> appeared. 'I will help you find your <object>,' they said.

# Together, they journeyed through <terrain> and faced the <weather_condition>. 

# Finally, they found the <object> in a <place2>. 

# The <animal> was so <emotion2> and thanked the <character>. 

# They lived <adverb> ever after.