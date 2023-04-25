from art import logo
from art import vs
from game_data import data
import random
print(logo)

def count_points(points):
    points += 1
    return points

def random_pj():
    top = 51
    pj = random.choice(data)
    data.pop(rand)
    top -= 1
    return pj

def value_bool(a, b):
    return a['follower_count'] - b['follower_count']

def game(a):
    points = 0;
    while (1):
        b =  random.choice(data)
        if points > 0:
            print(f"You`re right! Current score: {points}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        c = input("Who has more followers? Type 'A' or 'B': ")
        if c == 'A' and value_bool(a, b) > 0:
            print("YOU WIN")
            points = count_points(points)
        elif c == 'B' and value_bool(a, b) < 0:
            print("YOU WIN")
            points = count_points(points)
            a = b
        else:
            print("YOU LOSE")
            break
        
a =  random.choice(data)
game(a)