TextReplacement = {}
userinloop = True

print(TextReplacement) #to check whether the code works or not


def Command():
    UserNavigationInput = str(input("Enter nav: ")).lower()
    return UserNavigationInput

def EditShortcut(n):
    if n == "add shortcut":
        shortcut = str(input("Enter shortcut: "))
        replacement = str(input("Enter shortcut: "))
        TextReplacement.update({shortcut:replacement})
    elif n == "remove shortcut":
        TextReplacement.pop(Command())
    else:
        print("Unidentified method please chooose from the following\n blah blah placeholder")


# Main loop
while userinloop:
    print("User commands:\n exit - to exit the cli\n edit shortcuts - to edit shortcuts")
    if Command() == "exit":
        print("Exiting CLi")
        userinloop = False
    elif Command() == "edit shortcuts":
        print(f"{TextReplacement}\n remove shortcut - to remove shortcut")
        if Command() == "remove shortcut":
            print(f"{TextReplacement}\n choose the shortcut you want to remove\n {EditShortcut(Command())}")
                         
    else:
        break

takeinput = str(input(""))

