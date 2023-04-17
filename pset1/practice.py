# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:18:19 2022

@author: Rowan
"""

with open("ps1_cow_data.txt", 'r') as f:
    cow_data = []
    for line in f:
        cow_data.append(line.strip())
        
            
data_list = []
for item in cow_data:
    data_list.append([cow for cow in item.split(',')])
    
    
cow_dic = {}
for item in data_list:
    cow_dic[item[0]] = item[1]

weight = 10

# print(cow_dic.get(first_cow,0))

cows_copy = {cow: weight for cow, weight in sorted(cow_dic.items(), key = lambda item: item[1], reverse = True)}
print(cows_copy)
print(cow_dic)

def greedycow(cows, weight=10):
    cows_copy = {cow: weight for cow, weight in sorted(cows.items(), key = lambda item: item[1], reverse = True)}
    avail_weight = weight
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
    return trips + greedycow(cows_copy, 10)

print(greedycow(cow_dic, 10))
# print(cow_dic)
# print(first_cow)        
    
    
    