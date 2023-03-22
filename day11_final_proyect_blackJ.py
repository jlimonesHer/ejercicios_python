# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day11_final_proyect_blackJ.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jlimones <jlimones@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/15 10:58:01 by user              #+#    #+#              #
#    Updated: 2023/03/20 08:06:14 by jlimones         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from imports.art import logo
import random
import sys
print(logo)
print("Welcome to BlackJack")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def choose_cards(total_cards):
    """Dar cartas aleatorias"""
    total_cards.append(random.choice(cards))

def score(cards_list):
    """Contar puntos de la mano"""
    card_score = 0
    for card in cards_list:
        card_score += card
    return card_score

def change_as(cards_list):
    """Si la puntuacion es mayor que 21 y existe un as cambia su valor a 1"""
    for card in cards_list:
        if score(cards_list) > 21 and card == 11:
            return score(cards_list) - 10
        else:
            return score(cards_list)
            

def add_card_player(num_cards_your, ask_for_cards):
    """Añade caratas a la mano del jugador"""
    while num_cards_your < ask_for_cards:
        choose_cards(your_cards)
        num_cards_your += 1
    return num_cards_your

def add_card_com(num_cards_com, ask_for_cards):
    """Añade caratas a la mano de la computadora"""
    while num_cards_com < ask_for_cards:
        choose_cards(com_cards)
        num_cards_com += 1
    return num_cards_com

def print_score_player(your_cards, com_cards):
    """Muestra por pantalla las puntuaciones de los jugadores"""
    print(f"your cards {your_cards}, current score: {change_as(your_cards)}")
    print(f"[X, {com_cards[1]}]")
    print(f"the score of com is, {change_as(com_cards)}")
    
def print_score_com(your_cards, com_cards):
    """Muestra por pantalla las puntuaciones de los jugadores"""
    print(f"your cards {your_cards}, current score: {change_as(your_cards)}")
    print(f"the cards of com: {com_cards}, current score: {change_as(com_cards)}")
            
player = input("Do you want to play a game of BlackJack? Type 'y' or 'n'.")
flag_reference = "y"
flag = False
ask_for_cards = 2
num_cards_your = 0
num_cards_com = 0
your_cards = []
com_cards = []

num_cards_your = add_card_player(num_cards_your, ask_for_cards)
add_card_com(num_cards_com, ask_for_cards)
your_score = change_as(your_cards)
com_score = change_as(com_cards)
if player == "n":
    flag = True
    sys.exit()
while flag == False:
    if player == "y" and your_score < 21:
        print_score_player(your_cards, com_cards)
    if change_as(com_cards) < 21:
        flag_reference = input("do you want another card? Type 'y' or 'n'")
        ask_for_cards += 1
    if flag_reference == "y" and change_as(your_cards) < 22:
        add_card_player(num_cards_your, ask_for_cards)
        num_cards_your += 1
    if flag_reference == "n" or change_as(your_cards) > 21:
        flag = True

ask_for_cards = 1
flag = False
while flag == False:
    if change_as(com_cards) < 21 and change_as(com_cards) <= 16:
        ask_for_cards += 1
        print(f"num_cards_com{num_cards_com}")
        print(f"ask_for_cards{ask_for_cards}")
        num_cards_com += 1
        add_card_com(num_cards_com, ask_for_cards)
        print_score_com(your_cards, com_cards)
    else:
        flag = True   
print(f"current score: {change_as(your_cards)}")
print(f"the score of com is {com_cards}")
if change_as(your_cards) > change_as(com_cards) and change_as(your_cards) <= 21:
    print("You win")
elif change_as(your_cards) > 21:
    print("You lose")
elif change_as(your_cards) < change_as(com_cards):
    print("You lose")
elif change_as(your_cards) == change_as(com_cards):
    print("the game is a draw")