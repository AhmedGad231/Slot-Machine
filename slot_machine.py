import random
import time

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


# Function to check winnings based on the symbols in each column
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # iterate upon the number of lines
        symbol = columns[0][line]  # symbol equal to the first symbol of each line
        for column in columns:  # Check the rest of symbols of the row to the symbol variable
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, value in symbols.items():
        for _ in range(value):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    print(columns)

    return columns


# Function to print the current slot machine configuration
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# Function to handle user deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


# Function to get the bet amount from the user
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


# Function to simulate the spinning of the slot machine
def spin(balance):
    if balance == 0:
        print("Your balance is zero. Please make a deposit.")
        balance += deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance, your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}.")
    print("\nSpinning the reels...")

    for _ in range(3):
        print_slot_machine(get_slot_machine_spin(ROWS, COLS, symbol_value))
        time.sleep(1)
        print("\n")

    print("Result:")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    balance += winnings
    print(f"You won on lines:", *winning_lines)
    return balance - total_bet


# Function to display the rules of the game
def display_rules():
    print("Welcome to the Slot Machine Game!")
    print("Rules:")
    print("1. You can bet on 1 to {0} lines.".format(MAX_LINES))  # MAX_Lines = 3
    print("2. The bet amount must be between $ {0} and $ {1}".format(MIN_BET, MAX_BET))  # Min_bet = 1 , Max_lines = 100
    print("3. The symbols and their values are:")
    for symbol, value in symbol_value.items():
        print("  {0}: {1}".format(symbol, value))  # A:5 , B:4 , C:3 , D:2
    print("4. You win by getting the same symbol on all lines in a column.")
    print("5. The winnings are calculated based on the symbol value and bet amount.")
    print("\nGood luck!\n")


def main():
    display_rules()  # Display the rules of the game

    balance = deposit()  # Make a deposit and assigned it to the balance

    while True:
        if balance < 0:  # Check if balance has a negative value
            balance = 0
        print(f"Current balance is : ${balance}")
        answer = input("Press enter any key to play or Press (q to quit), or (r to view rules).")  # key to start game
        if answer.lower() == 'q':  # Quit
            break
        elif answer.lower() == 'r':  # View the Rules
            display_rules()
        else:
            balance = spin(balance)  # Update balance with the returned value from spin()
    print(f"You left with ${balance}")   # the left balance


main()  # Call the main function to start the game
