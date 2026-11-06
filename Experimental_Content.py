# User_message = str(input('Enter Message'))
TextReplacement = {"set": "key","money":"no"}
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

if Command() == "remove shortcut":
    print(f"Which shortcut would you like to remove {TextReplacement}")
    EditCommand(Command())    
    print(TextReplacement)
else:
    print("Over")

takeinput = str(input(""))

