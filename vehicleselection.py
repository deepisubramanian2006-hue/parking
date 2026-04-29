print("==== Parking System ====")
print("1. Two Wheeler")
print("2. Four Wheeler")

choice = int(input("Select Vehicle Type (1 or 2): "))

if choice == 1:
    print("You selected Two Wheeler Parking")
elif choice == 2:
    print("You selected Four Wheeler Parking")
else:
    print("Invalid Choice")
