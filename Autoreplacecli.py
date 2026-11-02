# User_message = str(input('Enter Message'))
Text_replacement = {
    "word": "replacement"
}
userinloop = True

print(Text_replacement) #to check whether the code works or not

def new_shortcut():
    shortcut = str(input("Enter shortcut"))
    replacement = str(input("Enter shortcut"))

    Text_replacement.update({shortcut:replacement})

# Main loop
while userinloop:
    usernav = str(input("Enter nav: ")).lower
    if usernav == "exit":
        userinloop = False
    elif usernav == "new shortcut":
        shortcut = str(input("Enter shortcut"))
        replacement = str(input("Enter replcement"))
        
        Text_replacement.update({shortcut:replacement})
    else:
        break

