tot_conc_volume = 0
conc_volume = 0
height = 0
length = 0
depth = 0

# Asks the user what the building type is and checks for "x"
build_type = input("What is the building type? (residential or commercial)")
while build_type.lower() != "x":
    if build_type.lower() == "residential":
        depth = 0.25
        # Error proofing code so that height and length doesn't break
        # when anything but an integer is entered
        try:
            height = int(input("What is the height? (m)"))
        except ValueError:
            print("That wasn't a number!")
            height = float(input("What is the height? (m)"))
        try:
            length = int(input("What is the width (m)"))
        except ValueError:
            print("That wasn't a number!")
            length = float(input("What is the width (m)"))
        conc_volume = height * length * depth
        print(f"The total amount of concrete needed is {conc_volume}m")
        tot_conc_volume += conc_volume
        # The code is essentially the same for commercial
    elif build_type.lower() == "commercial":
        depth = 0.5
        try:
            height = int(input("What is the height? (m)"))
        except ValueError:
            print("That wasn't a number!")
            height = float(input("What is the height? (m)"))
        try:
            length = float(input("What is the width (m)"))
        except ValueError:
            print("That wasn't a number!")
            length = int(input("What is the width (m)"))
        conc_volume = height * length * depth
        print(f"The total amount of concrete needed is {conc_volume}m")
        tot_conc_volume += conc_volume
    else:
        print("Please enter either residential or commercial")
    build_type = input("What is the building type? (residential or commercial)")

print(f"Total concrete volume needed is {tot_conc_volume}m")
