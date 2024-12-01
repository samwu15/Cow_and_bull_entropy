#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:37:03 2024

@author: wujiayou
"""


import random
import itertools
import math
from collections import Counter

# generate possible answers
def generate_possible_answers():
    return [''.join(map(str, digits)) for digits in itertools.permutations(range(10), 4)]

# evaluate the value of (bulls, cows)
def evaluate_guess(answer, guess):
    bulls = sum(1 for a, g in zip(answer, guess) if a == g)
    cows = sum(1 for g in guess if g in answer) - bulls
    return (bulls, cows)

# calculate entropy
def calculate_entropy(possible_answers, guess):
    if len(possible_answers) == 1:
        return 0.0
    # calculate frequency of every (bulls, cows) 
    results = [evaluate_guess(answer, guess) for answer in possible_answers]
    # count the frequency of each (bulls, cows)
    counter = Counter(results) 
    total_results = sum(counter.values())
    # calculate the probability 
    
    probabilities = [freq / total_results for freq in counter.values()]
    
    print(f"Total result:{total_results}")
    print(f"(Bulls, Cows) Distribution: {counter}\n")
    print(f"(Bulls, Cows) Probabilities: {probabilities}\n")
   
    
    # formula of entropy: H = -Σ(p_i * log2(p_i))
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

def main():
    print("Welcome to Bulls and Cows!")
    print("Try to guess the 4-digit number.")
    global possible_answers  # global 
    
    while True:
        # input the guess
        guess = input("Enter a 4-digit number: ")
        
        # test whether the value is vaild or not
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input. Please enter exactly 4 digits.")
            continue
        
        # evaluate the guess value of (bulls, cows)
        bulls, cows = evaluate_guess(answer, guess)
        print(f"Bulls: {bulls}")
        print(f"Cows: {cows}")
        
        # the condition to end
        if bulls == 4:
            print(f"You got it!!! The answer was: {answer}")
            break
        
        # calculate the entropy
        entropy = calculate_entropy(possible_answers, guess)
        print(f"Entropy after guessing '{guess}' is {entropy:.4f}")
        
        
        # renew the possible answer by evaluate bulls and cows
        possible_answers = [
            i for i in possible_answers
            if evaluate_guess(i, guess) == (bulls, cows)
        ]
        #provide a readable possible answer pool to help palyer 
        if len(possible_answers)<=10:
            print(f"Recommend answer:{possible_answers}")
        # count the numer in the possible answer pool
        print(f"Remaining possible answers: {len(possible_answers)}")
        print("-------------------------------------------------------")
        
        
        
# random generate a answer
answer = ''.join(map(str, random.sample(range(10), 4)))
possible_answers = generate_possible_answers()


print(f"Answer is {answer}")
# 
if __name__=='__main__':

    main()
