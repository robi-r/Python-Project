import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 7
}

symbol_values = {
    "A": 5,
    "B": 2,
    "C": 3,
    "D": 1
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range( lines ):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings,winning_lines



def get_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
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
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = " | ")

        print()


def deposit():
    while True:
        amount = input("What Is your Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount has to be greater than 0.")
        else:
            print("Please enter a number.")
    return amount



def get_the_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid amount of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
     while True:
        amount = input("What Is your Bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"The amount has to be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    

def spin(balance):
   
   lines = get_the_lines()
   while True:
       bet = get_bet()
       total_bet = bet * lines
       if total_bet > balance:
           print(f"Not enough balance. Your current balance is ${balance} ")
       else:
           break
      
   
   print(f"You are betting ${bet} on {lines} lines. total bet is equal to: ${total_bet} ")


   slots = get_spin(ROWS,COLS,symbol_count)
   print_slot_machine(slots)
   winnings, winning_lines = check_winning(slots,lines,bet,symbol_values)

   print(f"You won ${winnings}.")
   print(f"You won on lines:", *winning_lines)
   
   return winnings - total_bet


def main():
   balance = deposit()
   while True:
       print(f"Current balance is ${balance}")
       ans = input("Press Enter to play(q to quit).")
       if ans == "q":
           break
       balance += spin(balance)

   print(f"You have ${balance}")

main()