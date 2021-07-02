print("Welcome to R language translator!")
num = int((input("How many phrases do you want to translate? ")))

for x in range(num):
    phrase = str((input("Enter any phrase: ")))
    #Translate into R language
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter.lower() in "aeiou": #if letter in "AEIOUaeiou":
                if letter.isupper():
                    translation = translation + "R"
                else:
                    translation = translation + "r"
            else:
                translation = translation + letter
        print(f'The final output is: {translation}')
        
    translate(phrase)








