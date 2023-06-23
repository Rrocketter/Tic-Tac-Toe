import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_board():
    print("Current Board:")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))
    print("   |   |   ")

def winning_system():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        exit()

# Function to check for a draw
def check_draw(board):
    # Check if the board is full
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

print("Welcome to Tic-Tac-Toe!")

beginning_userChoice = input("Do you want to play against a friend or the computer?")

if beginning_userChoice == "friend":
    user1_name = input("Player 1, what is your name?")
    user2_name = input("Player 2, what is your name?")
    print("Hello " + user1_name + " and " + user2_name + "!")
    print("Let's play Tic-Tac-Toe! May the best person win!")

    print_board()

    print(user1_name + ", you are X's and " + user2_name + ", you are O's.")
    print("You will take turns and will say either Top, Middle, or Bottom, and then Left, Middle, or Right.")
    print("For example, if you want to put your X or O in the top left corner, you would say tl.")
    print("Let's begin!")

    #user1's choice
    user1_choice = input(user1_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user1_choice)

    # Update the board based on user1's choice
    if user1_choice == "tl":
        board[0][0] = 'X'
    elif user1_choice == "tm":
        board[0][1] = 'X'
    elif user1_choice == "tr":
        board[0][2] = 'X'
    elif user1_choice == "ml":
        board[1][0] = 'X'
    elif user1_choice == "mm":
        board[1][1] = 'X'
    elif user1_choice == "mr":
        board[1][2] = 'X'
    elif user1_choice == "bl":
        board[2][0] = 'X'
    elif user1_choice == "bm":
        board[2][1] = 'X'
    elif user1_choice == "br":
        board[2][2] = 'X'
    else:
        print("Invalid choice, you lose! " + user2_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    #user2's choice
    user2_choice = input(user2_name + ", what is your choice?")
    print(user2_name + ", your choice is " + user2_choice)

    # Update the board based on user2's choice
    if user2_choice == "tl":
        board[0][0] = 'O'
    elif user2_choice == "tm":
        board[0][1] = 'O'
    elif user2_choice == "tr":
        board[0][2] = 'O'
    elif user2_choice == "ml":
        board[1][0] = 'O'
    elif user2_choice == "mm":
        board[1][1] = 'O'
    elif user2_choice == "mr":
        board[1][2] = 'O'
    elif user2_choice == "bl":
        board[2][0] = 'O'
    elif user2_choice == "bm":
        board[2][1] = 'O'
    elif user2_choice == "br":
        board[2][2] = 'O'
    elif user2_choice == user1_choice:
        print("Invalid choice, you lose! " + user1_name + " already chose this and automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose!")
        exit()

    print_board()
    winning_system()

    # user1's choice 2nd choice

    user1_choice2 = input(user1_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user1_choice2)

    # Update the board based on user1's 2nd choice
    if user1_choice2 == "tl":
        board[0][0] = 'X'
    elif user1_choice2 == "tm":
        board[0][1] = 'X'
    elif user1_choice2 == "tr":
        board[0][2] = 'X'
    elif user1_choice2 == "ml":
        board[1][0] = 'X'
    elif user1_choice2 == "mm":
        board[1][1] = 'X'
    elif user1_choice2 == "mr":
        board[1][2] = 'X'
    elif user1_choice2 == "bl":
        board[2][0] = 'X'
    elif user1_choice2 == "bm":
        board[2][1] = 'X'
    elif user1_choice2 == "br":
        board[2][2] = 'X'
    elif user1_choice2 == user2_choice or user1_choice2 == user1_choice:
        print("Invalid choice, your move has already been played before. You lose! "
              + user2_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user2_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user2's 2nd choice

    user2_choice2 = input(user2_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user2_choice2)

    # Update the board based on user2's 2nd choice
    if user2_choice2 == "tl":
        board[0][0] = 'O'
    elif user2_choice2 == "tm":
        board[0][1] = 'O'
    elif user2_choice2 == "tr":
        board[0][2] = 'O'
    elif user2_choice2 == "ml":
        board[1][0] = 'O'
    elif user2_choice2 == "mm":
        board[1][1] = 'O'
    elif user2_choice2 == "mr":
        board[1][2] = 'O'
    elif user2_choice2 == "bl":
        board[2][0] = 'O'
    elif user2_choice2 == "bm":
        board[2][1] = 'O'
    elif user2_choice2 == "br":
        board[2][2] = 'O'
    elif user2_choice2 == user2_choice or user2_choice2 == user1_choice2 or user2_choice2 == user1_choice:
        print("Invalid choice, your move has already been played before. You lose! "
              + user1_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user1_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user1's 3rd choice

    user1_choice3 = input(user1_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user1_choice3)

    # Update the board based on user1's 3rd choice
    if user1_choice3 == "tl":
        board[0][0] = 'X'
    elif user1_choice3 == "tm":
        board[0][1] = 'X'
    elif user1_choice3 == "tr":
        board[0][2] = 'X'
    elif user1_choice3 == "ml":
        board[1][0] = 'X'
    elif user1_choice3 == "mm":
        board[1][1] = 'X'
    elif user1_choice3 == "mr":
        board[1][2] = 'X'
    elif user1_choice3 == "bl":
        board[2][0] = 'X'
    elif user1_choice3 == "bm":
        board[2][1] = 'X'
    elif user1_choice3 == "br":
        board[2][2] = 'X'
    elif user1_choice3 == user2_choice or user1_choice3 == user1_choice2 or user1_choice3 == user1_choice or user1_choice3 == user2_choice2:
        print("Invalid choice, your move has already been played before. You lose! "
              + user2_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user2_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user2's 3rd choice

    user2_choice3 = input(user1_name + ", what is your choice?")
    print(user2_name + ", your choice is " + user2_choice3)
    # Update the board based on user2's 3rd choice
    if user2_choice3 == "tl":
        board[0][0] = 'O'
    elif user2_choice3 == "tm":
        board[0][1] = 'O'
    elif user2_choice3 == "tr":
        board[0][2] = 'O'
    elif user2_choice3 == "ml":
        board[1][0] = 'O'
    elif user2_choice3 == "mm":
        board[1][1] = 'O'
    elif user2_choice3 == "mr":
        board[1][2] = 'O'
    elif user2_choice3 == "bl":
        board[2][0] = 'O'
    elif user2_choice3 == "bm":
        board[2][1] = 'O'
    elif user2_choice3 == "br":
        board[2][2] = 'O'
    elif user2_choice3 == user2_choice or user2_choice3 == user1_choice2 or user2_choice3 == user1_choice or user2_choice3 == user2_choice2 or user2_choice3 == user1_choice3:
        print("Invalid choice, your move has already been played before. You lose! "
              + user1_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user1_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user1's 4th choice

    user1_choice4 = input(user1_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user1_choice4)

    # Update the board based on user1's 4th choice
    if user1_choice4 == "tl":
        board[0][0] = 'X'
    elif user1_choice4 == "tm":
        board[0][1] = 'X'
    elif user1_choice4 == "tr":
        board[0][2] = 'X'
    elif user1_choice4 == "ml":
        board[1][0] = 'X'
    elif user1_choice4 == "mm":
        board[1][1] = 'X'
    elif user1_choice4 == "mr":
        board[1][2] = 'X'
    elif user1_choice4 == "bl":
        board[2][0] = 'X'
    elif user1_choice4 == "bm":
        board[2][1] = 'X'
    elif user1_choice4 == "br":
        board[2][2] = 'X'
    elif user1_choice4 == user1_choice or user1_choice4 == user1_choice2 or user1_choice4 == user1_choice3 or user1_choice4 == user2_choice or user1_choice4 == user2_choice2 or user1_choice4 == user2_choice3:
        print("Invalid choice, your move has already been played before. You lose! "
              + user2_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user2_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user2's 4th choice

    user2_choice4 = input(user2_name + ", what is your choice?")
    print(user2_name + ", your choice is " + user2_choice4)
    # Update the board based on user2's 4th choice
    if user2_choice4 == "tl":
        board[0][0] = 'O'
    elif user2_choice4 == "tm":
        board[0][1] = 'O'
    elif user2_choice4 == "tr":
        board[0][2] = 'O'
    elif user2_choice4 == "ml":
        board[1][0] = 'O'
    elif user2_choice4 == "mm":
        board[1][1] = 'O'
    elif user2_choice4 == "mr":
        board[1][2] = 'O'
    elif user2_choice4 == "bl":
        board[2][0] = 'O'
    elif user2_choice4 == "bm":
        board[2][1] = 'O'
    elif user2_choice4 == "br":
        board[2][2] = 'O'
    elif user2_choice4 == user1_choice or user2_choice4 == user1_choice2 or user2_choice4 == user1_choice3 or user2_choice4 == user1_choice4 or user2_choice4 == user2_choice or user2_choice4 == user2_choice2 or user2_choice4 == user2_choice3:
        print("Invalid choice, your move has already been played before. You lose! "
              + user1_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user1_name + " automatically wins!")
        exit()

    print_board()
    winning_system()

    # user1's 5th choice

    user1_choice5 = input(user1_name + ", what is your choice?")
    print(user1_name + ", your choice is " + user1_choice5)

    # Update the board based on user1's 5th choice
    if user1_choice5 == "tl":
        board[0][0] = 'X'
    elif user1_choice5 == "tm":
        board[0][1] = 'X'
    elif user1_choice5 == "tr":
        board[0][2] = 'X'
    elif user1_choice5 == "ml":
        board[1][0] = 'X'
    elif user1_choice5 == "mm":
        board[1][1] = 'X'
    elif user1_choice5 == "mr":
        board[1][2] = 'X'
    elif user1_choice5 == "bl":
        board[2][0] = 'X'
    elif user1_choice5 == "bm":
        board[2][1] = 'X'
    elif user1_choice5 == "br":
        board[2][2] = 'X'
    elif user1_choice5 == user1_choice or user1_choice5 == user1_choice2 or user1_choice5 == user1_choice3 or user1_choice5 == user1_choice4 or user1_choice5 == user2_choice or user1_choice == user2_choice2 or user1_choice5 == user2_choice3 or user1_choice5 == user2_choice4:
        print("Invalid choice, your move has already been played before. You lose! "
              + user2_name + " automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! " + user2_name + " automatically wins!")
        exit()

    print_board()
    winning_system()
    if check_draw(board):
        print("The game ends in a draw.")

if beginning_userChoice == "computer":
    print("Hello! You will be playing tic tac toe against the computer. You will be Player 1 play as X's and the computer will be Player 2 and play as O's.")

    print("You will take turns and will say either Top, Middle, or Bottom, and then Left, Middle, or Right.")
    print("For example, if you want to put your X or O in the top left corner, you would say tl.")
    print("Let's begin!")

    print_board()

    # player 1's first move
    player1_choice = input("What is your choice?")
    print("Player 1, your choice is " + player1_choice)

    # Update the board based on player 1's first choice
    if player1_choice == "tl":
        board[0][0] = 'X'
    elif player1_choice == "tm":
        board[0][1] = 'X'
    elif player1_choice == "tr":
        board[0][2] = 'X'
    elif player1_choice == "ml":
        board[1][0] = 'X'
    elif player1_choice == "mm":
        board[1][1] = 'X'
    elif player1_choice == "mr":
        board[1][2] = 'X'
    elif player1_choice == "bl":
        board[2][0] = 'X'
    elif player1_choice == "bm":
        board[2][1] = 'X'
    elif player1_choice == "br":
        board[2][2] = 'X'
    else:
        print("Invalid choice, you lose! The computer automatically wins!")
        exit()

    print_board()
    winning_system()

    # computer's random system and first move
    computer_choice1 = random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    while computer_choice1 == player1_choice:
        random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    print("The computer's choice is " + computer_choice1)
    if computer_choice1 == "tl":
        board[0][0] = 'O'
    elif computer_choice1 == "tm":
        board[0][1] = 'O'
    elif computer_choice1 == "tr":
        board[0][2] = 'O'
    elif computer_choice1 == "ml":
        board[1][0] = 'O'
    elif computer_choice1 == "mm":
        board[1][1] = 'O'
    elif computer_choice1 == "mr":
        board[1][2] = 'O'
    elif computer_choice1 == "bl":
        board[2][0] = 'O'
    elif computer_choice1 == "bm":
        board[2][1] = 'O'
    elif computer_choice1 == "br":
        board[2][2] = 'O'

    print_board()
    winning_system()

    # player 1's second move
    player1_choice2 = input("What is your choice?")
    print("Player 1, your choice is " + player1_choice2)

    # Update the board based on player 1's second move
    if player1_choice2 == "tl":
        board[0][0] = 'X'
    elif player1_choice2 == "tm":
        board[0][1] = 'X'
    elif player1_choice2 == "tr":
        board[0][2] = 'X'
    elif player1_choice2 == "ml":
        board[1][0] = 'X'
    elif player1_choice2 == "mm":
        board[1][1] = 'X'
    elif player1_choice2 == "mr":
        board[1][2] = 'X'
    elif player1_choice2 == "bl":
        board[2][0] = 'X'
    elif player1_choice2 == "bm":
        board[2][1] = 'X'
    elif player1_choice2 == "br":
        board[2][2] = 'X'
    elif player1_choice2 == player1_choice or player1_choice2 == computer_choice1:
        print("Invalid choice, you lose! Your move has already been played before. The computer automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! The computer automatically wins!")
        exit()

    print_board()
    winning_system()

    # computer's 2nd move
    computer_choice2 = random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    while computer_choice2 == player1_choice or computer_choice2 == computer_choice1 or computer_choice2 == player1_choice2:
        random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    print("The computer's choice is " + computer_choice2)
    if computer_choice2 == "tl":
        board[0][0] = 'O'
    elif computer_choice2 == "tm":
        board[0][1] = 'O'
    elif computer_choice2 == "tr":
        board[0][2] = 'O'
    elif computer_choice2 == "ml":
        board[1][0] = 'O'
    elif computer_choice2 == "mm":
        board[1][1] = 'O'
    elif computer_choice2 == "mr":
        board[1][2] = 'O'
    elif computer_choice2 == "bl":
        board[2][0] = 'O'
    elif computer_choice2 == "bm":
        board[2][1] = 'O'
    elif computer_choice2 == "br":
        board[2][2] = 'O'

    print_board()
    winning_system()

    # player 1's third move

    player1_choice3 = input("What is your choice?")
    print("Player 1, your choice is " + player1_choice3)

    # Update the board based on player 1's third move
    if player1_choice3 == "tl":
        board[0][0] = 'X'
    elif player1_choice3 == "tm":
        board[0][1] = 'X'
    elif player1_choice3 == "tr":
        board[0][2] = 'X'
    elif player1_choice3 == "ml":
        board[1][0] = 'X'
    elif player1_choice3 == "mm":
        board[1][1] = 'X'
    elif player1_choice3 == "mr":
        board[1][2] = 'X'
    elif player1_choice3 == "bl":
        board[2][0] = 'X'
    elif player1_choice3 == "bm":
        board[2][1] = 'X'
    elif player1_choice3 == "br":
        board[2][2] = 'X'
    elif player1_choice3 == player1_choice or player1_choice3 == computer_choice1 or player1_choice3 == computer_choice2 or player1_choice3 == player1_choice2:
        print("Invalid choice, you lose! Your move has already been played before. The computer automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! The computer automatically wins!")
        exit()

    print_board()
    winning_system()

    # computer's 3rd move
    computer_choice3 = random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    while computer_choice3 == player1_choice or computer_choice3 == computer_choice1 or computer_choice3 == player1_choice2 or computer_choice3 == computer_choice2 or computer_choice3 == player1_choice3:
        random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    print("The computer's choice is " + computer_choice3)
    if computer_choice3 == "tl":
        board[0][0] = 'O'
    elif computer_choice3 == "tm":
        board[0][1] = 'O'
    elif computer_choice3 == "tr":
        board[0][2] = 'O'
    elif computer_choice3 == "ml":
        board[1][0] = 'O'
    elif computer_choice3 == "mm":
        board[1][1] = 'O'
    elif computer_choice3 == "mr":
        board[1][2] = 'O'
    elif computer_choice3 == "bl":
        board[2][0] = 'O'
    elif computer_choice3 == "bm":
        board[2][1] = 'O'
    elif computer_choice3 == "br":
        board[2][2] = 'O'

    print_board()
    winning_system()

    # player 1's fourth move
    player1_choice4 = input("What is your choice?")
    print("Player 1, your choice is " + player1_choice4)

    # Update the board based on player 1's fourth move
    if player1_choice4 == "tl":
        board[0][0] = 'X'
    elif player1_choice4 == "tm":
        board[0][1] = 'X'
    elif player1_choice4 == "tr":
        board[0][2] = 'X'
    elif player1_choice4 == "ml":
        board[1][0] = 'X'
    elif player1_choice4 == "mm":
        board[1][1] = 'X'
    elif player1_choice4 == "mr":
        board[1][2] = 'X'
    elif player1_choice4 == "bl":
        board[2][0] = 'X'
    elif player1_choice4 == "bm":
        board[2][1] = 'X'
    elif player1_choice4 == "br":
        board[2][2] = 'X'
    elif player1_choice4 == player1_choice or player1_choice4 == player1_choice2 or player1_choice4 == player1_choice3 or player1_choice4 == computer_choice1 or player1_choice4 == computer_choice2 or player1_choice4 == computer_choice3:
        print("Invalid choice, you lose! Your move has already been played before. The computer automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! The computer automatically wins!")
        exit()

    print_board()
    winning_system()

    # computer's 4th move
    computer_choice4 = random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    while computer_choice4 == player1_choice or computer_choice4 == computer_choice1 or computer_choice4 == player1_choice2 or computer_choice4 == computer_choice2 or computer_choice4 == player1_choice3 or computer_choice4 == computer_choice3 or computer_choice4 == player1_choice4:
        random.choice(["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    print("The computer's choice is " + computer_choice4)
    if computer_choice4 == "tl":
        board[0][0] = 'O'
    elif computer_choice4 == "tm":
        board[0][1] = 'O'
    elif computer_choice4 == "tr":
        board[0][2] = 'O'
    elif computer_choice4 == "ml":
        board[1][0] = 'O'
    elif computer_choice4 == "mm":
        board[1][1] = 'O'
    elif computer_choice4 == "mr":
        board[1][2] = 'O'
    elif computer_choice4 == "bl":
        board[2][0] = 'O'
    elif computer_choice4 == "bm":
        board[2][1] = 'O'
    elif computer_choice4 == "br":
        board[2][2] = 'O'

    print_board()
    winning_system()

    # player 1's fifth move (last move)
    player1_choice5 = input("What is your choice?")
    print("Player 1, your choice is " + player1_choice5)

    # Update the board based on player 1's fifth move
    if player1_choice5 == "tl":
        board[0][0] = 'X'
    elif player1_choice5 == "tm":
        board[0][1] = 'X'
    elif player1_choice5 == "tr":
        board[0][2] = 'X'
    elif player1_choice5 == "ml":
        board[1][0] = 'X'
    elif player1_choice5 == "mm":
        board[1][1] = 'X'
    elif player1_choice5 == "mr":
        board[1][2] = 'X'
    elif player1_choice5 == "bl":
        board[2][0] = 'X'
    elif player1_choice5 == "bm":
        board[2][1] = 'X'
    elif player1_choice5 == "br":
        board[2][2] = 'X'
    elif player1_choice5 == player1_choice or player1_choice5 == player1_choice2 or player1_choice5 == player1_choice3 or player1_choice5 == player1_choice4 or player1_choice5 == computer_choice1 or player1_choice5 == computer_choice2 or player1_choice5 == computer_choice3 or player1_choice5 == computer_choice4:
        print("Invalid choice, you lose! Your move has already been played before. The computer automatically wins!")
        exit()
    else:
        print("Invalid choice, you lose! The computer automatically wins!")
        exit()

    print_board()
    winning_system()
    if check_draw(board):
        print("The game ends in a draw.")

else:
    print("Invalid choice. Please select either 'friend' to play against a friend or 'computer' to play against the computer.")
    exit()
