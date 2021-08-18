from art import logo
from replit import clear

print(logo)

bidder_dict = {}
def find_highest(bidder_dict):
    highest = 0
    for bidder in bidder_dict:
        bid_amount = bidder_dict[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} and they won with a price of ${highest:.2f}")

while True:
    name = input("Please input the bidder's name. ")
    amount = float(input("Please input a bid price. "))
    bidder_dict[name] = amount
    winner = {}
    more = input("Are there other's that need to bid? Yes or No ").lower()
    if more == "yes":
        clear()
        continue
    elif more == "no":
        break
        # print(f"The winner is {bidder_dict[key]} with an amount of {bidder_dict[key[amount]]}")
        # break
find_highest(bidder_dict=bidder_dict)

    # elif more == "no":
