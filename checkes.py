player_1 = input("Enter your player_1 name: ")
player1_x_position = input(f"{player_1} Enter your x_position: ")
player1_y_position = input(f"{player_1} Enter your y_position: ")

if (player1_x_position.isdigit() and player1_y_position.isdigit()) and 1 <= int(player1_x_position) <= 8 and 1 <= int(player1_y_position) <= 8:
   player1_x_position = int(player1_x_position)
   player1_y_position = int(player1_y_position)

player_2 = input("Enter your player_2 name: ")
player2_x_position = input(f"{player_2} Enter your x_position: ")
player2_y_position = input(f"{player_2} Enter your y_position: ")

if (player2_x_position.isdigit()) and (player2_y_position.isdigit()) and 1 < int(player2_x_position) < 8 and 1 < int(player2_y_position) < 8:
    player2_x_position = int(player2_x_position)
    player2_y_position = int(player2_y_position)
    px = player1_x_position - player2_x_position
    py = player1_y_position - player2_y_position
    if (px == -1) and (py == 1) or (px == -1) and (py == -1) or (px == 1) and (py == 1) or (px == 1) and (py == -1):
        question = input(f"{player_1} Do you want cut {player_2} (yes/no): ")
        if(question == "yes"):
            print("cut", player_2)
            if (px == -1) and (py == -1):
                print('your new position (x): ', player1_x_position + 2, '(Y): ', player1_y_position + 2)
            elif (px == 1) and (py == 1):
                print('your new position (x): ', player1_x_position - 2, '(Y): ', player1_y_position - 2)
            elif (px == 1) and (py == -1):
                print('your new position (x): ', player1_x_position - 2, '(Y): ', player1_y_position + 2)
            elif (px == -1) and (py == 1):
                print('your new position (x): ', player1_x_position + 2, '(Y): ', player1_y_position - 2)
        else:
            print("invalid input")
    else:
        print("cant cut")
else:
    print("invalid")
