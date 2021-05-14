an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Just enter your name: ")
times = int(input("What is your enthusiasm level (1-10): "))

for char in word:
   if char in an_letters:
       print("Give me an " + char + "! " + char)
   else:
       print("Give me a  " + char + "! " + char)

print("What does that spell?")
for i in range(times):
   print(word, "!!!")
