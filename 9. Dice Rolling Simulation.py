import random
while True:
    dice = random.randint(1, 6)
    def roll(dice):
        sides = {
            1: "|     |\n|  0  |\n|     |",
            2: "|0    |\n|     |\n|    0|",
            3: "|0    |\n|  0  |\n|    0|",
            4: "|0   0|\n|     |\n|0   0|",
            5: "|0   0|\n|  0  |\n|0   0|",
            6: "|0   0|\n|0   0|\n|0   0|"
        }
        return sides.get(dice)

    user_input = (input(str("Do you want to roll the dice(yes/no)?: ")))
    if user_input == "yes":
        print("Rolling the dice............")
        print(roll(dice))
    else:
        print("Thanks for playing!")
        exit(0)