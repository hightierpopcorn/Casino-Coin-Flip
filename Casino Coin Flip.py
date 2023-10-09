#Christopher's Casino Heads or Tails
import random

money = 100



def coin_flip():

    print("Wanna play heads or tails?")
    print("Available money: " + "$", money)
    print('\n')
    bet = input("Please enter heads or tails: ")
    wager = input("Please Enter Your Wager: ")
    int_wager = int(wager)
    print("You Wagered: " + "$", int_wager, " on: ", bet)
    print('\n')
    winner = random.randint(1, 2)

    if bet == "heads" and winner == 1:
        cash_total = money + int_wager
        print("Winner: Heads! Your Cash Total: ", cash_total)
        return cash_total
    if bet == "tails" and winner == 2:
        cash_total = money + int_wager
        print("Winner: Tails! " + "Your Total: ", cash_total)
        return cash_total
    else:
        cash_total = money - int_wager
        print("LOSERR")
        print("cash total: ", cash_total)
        return cash_total


coin_flip()
