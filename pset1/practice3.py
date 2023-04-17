# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 18:29:25 2022

@author: Rowan
"""


# Problem 1

egg_weights = (1, 5, 10, 25)
n = 99

def dp_make_weight(egg_weights, target_weight, memo = {}):
# """
# Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
# an infinite supply of eggs of each weight, and there is always a egg of value 1.

# Parameters:
# egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
# target_weight - int, amount of weight we want to find eggs to fit
# memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

# Returns: int, smallest number of eggs needed to make target weight
# """
# # TODO: Your code here
# #memo could be - for any given available weight, what egg weights have been tried
# #need to have some sort of evaluation, what route is the best? - this would be based on total number of eggs
# #need a list of eggs stored and a record of how much weight is left

# #could be, try each 
# #ok so recursive function, for loop of all weights
# #list is built for each new addition
# #
    


    egg_weights = tuple(sorted(egg_weights, reverse = True))
    print(egg_weights)
    
    if egg_weights == () or target_weight == 0:
        result = 0
        print("empty list, returning zero")
        
    elif target_weight < egg_weights[0]:
        print("too big, going to next egg")
        result = dp_make_weight(egg_weights[1:],target_weight,memo)
        
    else:
        print("egg fits, continue with this egg")
        result = dp_make_weight(egg_weights, target_weight - egg_weights[0], memo)
        if egg_weights in memo:
            print("this weight set has been tried, adding one to result")
            return result + 1
    print("adding one to this egg weight set")    
    memo[egg_weights] = 1
    return result


if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()