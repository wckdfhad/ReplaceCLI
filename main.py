# User_message = str(input('Enter Message'))
TextReplacement = {}
userinloop = True

print(TextReplacement) #to check whether the code works or not

def EditShortcut():
    shortcut = str(input("Enter shortcut: "))
    replacement = str(input("Enter shortcut: "))

    TextReplacement.update({shortcut:replacement})

def EditCommand(n):
    TextReplacement.pop(n)


def Command():
    UserNavigationInput = str(input("Enter nav: ")).lower()
    return UserNavigationInput

# Main loop
while userinloop:
    print("User commands:\n exit - to exit the cli\n edit shortcuts - to edit shortcuts")
    if Command() == "exit":
        print("Exiting CLi")
        userinloop = False
    elif Command() == "edit shortcuts":
        print(f"{TextReplacement}\n remove shortcut - to remove shortcut")

        if Command() == "remove shortcut":
            EditCommand(Command())

    else:
        break

takeinput = str(input(""))

