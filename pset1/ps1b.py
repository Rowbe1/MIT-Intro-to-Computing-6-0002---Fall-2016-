###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    #I STOLE THIS CODE - except the print statements I added to help visualisation
    #I had the basic elements conceptually to build this, but I was reluctant to sort since I thought this would
    #just turn it into a greedy algorithm. I'm not totally sure what the memo is actually doing - will use python tutor
    #NOTE THAT THIS SOLUTION DOESN'T APPEAR TO REQUIRE THE MEMO. YOU CAN REMOVE THE MEMO AND GET THE SAME RESULT
    #NEED TO FIND A TRUE MEMOISATION SOLUTION. 
    #I really don't like this problem since it is totally amenable to a greedy solution.
    
    
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
        # if egg_weights in memo:
        #     print("this weight set has been tried, adding one to result")
        return result + 1
    print("adding one to this egg weight set", memo)    
    #memo[egg_weights] = 1
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()