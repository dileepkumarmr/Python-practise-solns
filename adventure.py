name = input("Enter your name: ")
print("Welcome", name, "to this addventure")

answer = input(" You are on a dirt road it has come to end and you can go left or right? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walk for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option.")
elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?  ")

    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
            answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
            if answer == "yes":
             print("You talk to the stranger and they give you gold. you WIN!")
            elif answer == "no":
                print("You ignore the stranger and they arre offended and you loose.")
            else:
                print("Not a valid option.You loose")
    else:
        print("Not a valid option.You loose")
else:
    print("Not a valid option.") 

print("Thank you for trying", name)