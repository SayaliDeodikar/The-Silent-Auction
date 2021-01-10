import auction_art
print(auction_art.logo)
from replit import clear
print("Welcome to 'The Silent Auction!'")
auction_records = {}
max = 0
winner = ""
should_continue = True
while should_continue:
    name = input("What's your name? ")
    bid = input("What's your bid? $")
    auction_records[name] = bid
    clear()
    choice = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if choice == 'no':
        should_continue = False
        for name in auction_records:
            if float(auction_records[name]) > float(max):
                max = auction_records[name]
                winner = name
                clear()
        print("Congratulations!!!")
        print(f"The winner is {winner} with a bid of ${max}")