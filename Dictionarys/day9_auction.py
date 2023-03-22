# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_auction.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: user <user@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/08 19:19:47 by user              #+#    #+#              #
#    Updated: 2022/11/08 19:21:51 by user             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secert auction program.")

auction = False
people_bid = {}
bidders = []
while auction == False:
    names = input("What is your name?: ")
    bid = int(input("what´s your bid? $"))
    people_bid[names] = bid;
    bidders.append(bid)
    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bidders == "no":
        auction = True
    bid_win = max(bidders)
    #clear()
    for name in people_bid:
        if bid_win == people_bid[name]:
            print(people_bid[name])
            name_winner = name
print(f"The winner is {name_winner} a bid of ${bid_win}")