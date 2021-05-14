x = str(input("Enter even to print even numbers and odd to print odd numbers: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

#for even numbers
if x == "even":
    for x in range (start,end):
        if x % 2 == 0:
            print(x)

#for odd numbers    
else:
    for x in range (start,end):
        if x % 2 != 0:
            print(x)


