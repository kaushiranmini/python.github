K = 13
Q = 12
J = 11
A = 1

player_1 = input("Enter player 1 name: ")
value = input("1. Enter your number: ")
total = 0

if value.isdigit() and 2 <= int(value) <= 10:
    total = int(value)
elif value == "Q" or value == "q":
        total = Q
elif value == "K" or value == "k":
    total = K
elif value == "J" or value == "j":
        total = J
elif value == "A" or value == "a":
        total = A
print(player_1, "total is: ", total)

chance = input("Do you want other chance(yes/no): ")
if chance == "yes":
    value = input("2. Enter your number: ")
if value.isdigit() and 2 <= int(value) <= 10:
    total += int(value)
    if value == "Q" or value == "q":
        total += Q
    elif value == "K" or value == "k":
        total += K
    elif value == "J" or value == "j":
        total += J
    elif value == "A" or value == "a":
        total += A
    print(player_1, "total is: ", total)
    chance = input("Do you want other chance(yes/no): ")
    if chance == "yes":
        value = input("3. Enter your number: ")
    if value.isdigit() and 2 <= int(value) <= 10:
        total += int(value)
        if value == "Q" or value == "q":
            total += Q
        elif value == "K" or value == "k":
            total += K
        elif value == "J" or value == "j":
            total += J
        elif value == "A" or value == "a":
            total += A
        print(player_1, "total is: ", total)

        chance = input("Do you want other chance(yes/no): ")
        if chance == "yes":
            value = input("4. Enter your number: ")
        if value.isdigit() and 2 <= int(value) <= 10:
            total += int(value)
            if value == "Q" or value == "q":
                total += Q
            elif value == "K" or value == "k":
                total += K
            elif value == "J" or value == "j":
                total += J
            elif value == "A" or value == "a":
                total += A
            print(player_1, "total is: ", total)

            if total > 31:
                print("You lost!!!")

    else:
        print("Invalid")
else:
    print("Invalid")


#player 2

player_2 = input("Enter player 1 name: ")
value = input("1. Enter your number: ")
total2 = 0

if value.isdigit() and 2 <= int(value) <= 10:
    total2 = int(value)
elif value == "Q" or value == "q":
    total2 = Q
elif value == "K" or value == "k":
    total2 = K
elif value == "J" or value == "j":
    total2 = J
elif value == "A" or value == "a":
    total2 = A
print(player_2, "total is: ", total2)

chance = input("Do you want other chance(yes/no): ")
if chance == "yes":
    value = input("2. Enter your number: ")
if value.isdigit() and 2 <= int(value) <= 10:
    total2 += int(value)
    if value == "Q" or value == "q":
        total2 += Q
    elif value == "K" or value == "k":
        total2 += K
    elif value == "J" or value == "j":
        total2 += J
    elif value == "A" or value == "a":
        total2 += A
    print(player_2, "total is: ", total2)
    chance = input("Do you want other chance(yes/no): ")
    if chance == "yes":
        value = input("3. Enter your number: ")
    if value.isdigit() and 2 <= int(value) <= 10:
        total2 += int(value)
        if value == "Q" or value == "q":
            total2 += Q
        elif value == "K" or value == "k":
            total2 += K
        elif value == "J" or value == "j":
            total2 += J
        elif value == "A" or value == "a":
            total2 += A
        print(player_2, "total is: ", total2)

        chance = input("Do you want other chance(yes/no): ")
        if chance == "yes":
            value = input("4. Enter your number: ")
        if value.isdigit() and 2 <= int(value) <= 10:
            total2 += int(value)
            if value == "Q" or value == "q":
                total2 += Q
            elif value == "K" or value == "k":
                total2 += K
            elif value == "J" or value == "j":
                total2 += J
            elif value == "A" or value == "a":
                total2 += A
            print(player_2, "total is: ", total2)

            if total2 > 31:
                print("You lost!!!")

    else:
        print("Invalid")
else:
    print("Invalid")