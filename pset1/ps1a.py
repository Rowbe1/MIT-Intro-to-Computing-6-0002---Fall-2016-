###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

filename = "ps1_cow_data.txt"

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename, 'r') as f:
        cow_data = []
        for line in f:
            cow_data.append(line.strip())
        
            
    data_list = []
    for item in cow_data:
        data_list.append([cow for cow in item.split(',')])
        
        
    cow_dic = {}
    for item in data_list:
        cow_dic[item[0]] = item[1]
        
    return cow_dic

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_copy = {cow: weight for cow, weight in sorted(cows.items(), key = lambda item: item[1], reverse = True)}
    avail_weight = limit
    trip = []
    trips = []
    if len(cows_copy) == 0:
        return trip
    else: 
        for cow in cows_copy:
            if int(cows_copy[cow]) < avail_weight:
                trip.append(cow)
                avail_weight -= int(cows_copy[cow])
        trips.append(trip)
        for cow in trip:
            del cows_copy[cow]
    return trips + greedy_cow_transport(cows_copy, 10)

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_journey = []
    for i in get_partitions(cows):
        good_journey = []
        tot_cows = 0
        for j in i:
            heft = 0
            for k in j:
                heft += int(cows.get(k))
            if heft <= 10:
                good_journey.append(j)
                tot_cows += len(j)
        if len(best_journey) == 0 and tot_cows == 10:
            best_journey = good_journey    
        elif len(good_journey) < len(best_journey) and tot_cows == 10:
            print("updating best", good_journey)
            best_journey = good_journey
    return best_journey
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cow_dic = load_cows(filename)
    greedy_start = time.time()
    greedy_trips = greedy_cow_transport(cow_dic, 10)
    greedy_end = time.time()
    greedy_time = greedy_end - greedy_start
    
    brute_start = time.time()
    brute_trips = brute_force_cow_transport(cow_dic, 10)
    brute_end = time.time()
    brute_time = brute_end - brute_start
    
    print("Greedy algo\n Number of trips: ", len(greedy_trips), "\n Time taken: ", greedy_time)
    print("Brute algo\n Number of trips: ", len(brute_trips), "\n Time taken: ", brute_time)
    
print(compare_cow_transport_algorithms())
