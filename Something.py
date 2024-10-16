


# no group work required think about the presentation grades or something 
print("\n\n\n Welcome to the Version Control Lab \n ------------------------------------------")

print("\n This program prints out the closest prime number to your input ")
userInput2 = input(" Enter your name: ")
userInput = int(input(" Enter a number: "))


if userInput % 2 == 0:
    print("Divisable by 2 not a prime number \n")
elif userInput % 3 == 0:
    print("Divisable by 3 not a prime number \n")
elif userInput % 4 == 0:
    print("Divisable by 4 not a prime number \n")
elif userInput % 5 == 0:
    print("Divisable by 5 not a prime number \n")
elif userInput % 6 == 0:
    print("Divisable by 6 not a prime number \n")
elif userInput % 7 == 0:
    print("Divisable by 7 not a prime number \n")
elif userInput % 8 == 0:
    print("Divisable by 8 not a prime number \n")
elif userInput % 9 == 0:
    print("Divisable by 9 not a prime number \n")
else:
    print(f"You typed a prime number {userInput2}! ")
    

# fstrings are ways to print with variables - formatted strings
# for prime number divided by 1 - 9 because if it can be divided by 15 it can be divided by 5 through LCM 
# iloc is a pandas function
# creating a data frame 