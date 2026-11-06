TextReplacement = {"Shortcut":"Replacement"}
userinloop = True

print(TextReplacement) #to check whether the code works or not


def Command():
    UserNavigationInput = str(input("Enter nav: ")).lower()
    return UserNavigationInput

def EditShortcut(n):
    if n == "adst":
        shortcut = str(input("Enter shortcut: "))
        replacement = str(input("Enter replacement: "))
        TextReplacement.update({shortcut:replacement})
    elif n == "rmst":
        TextReplacement.pop(Command())
    else:
        print("Unidentified method please chooose from the following\n blah blah placeholder")


# Main loop
while userinloop:
    print("User commands:\n exit - to exit the cli\n edst - to edit shortcuts")
    UserNavigation = Command()

    if UserNavigation == "edst":
        print(f"{TextReplacement}\n rmst - to remove shortcut\n adst - to add shortcut\n")
        EditShortcut(Command())
        
    
    elif UserNavigation == "exit":
            print("Exiting CLi")
            userinloop = False         

    else:
        break


