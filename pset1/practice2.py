# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:04:11 2022

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

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
        
        


cow_list = []
for cow in cow_dic:
    cow_list.append(cow)

good_journey = []
best_journey = []
heft = 0
tot_heft = 0

print(len(cow_dic))
wgt = 0
for item in cow_dic:
    wgt += int(cow_dic.get(item))

print(wgt)

for i in get_partitions(cow_dic):
    good_journey = []
    tot_cows = 0
    #print(i)
    for j in i:
        heft = 0
        for k in j:
            heft += int(cow_dic.get(k))
        if heft <= 10:
            good_journey.append(j)
            tot_cows += len(j)
            #print(j)
            #print(tot_cows)
            #print("good_journey", good_journey)
    if len(best_journey) == 0 and tot_cows == 10:
        best_journey = good_journey    
    elif len(good_journey) < len(best_journey) and tot_cows == 10:
        print("updating best", good_journey)
        best_journey = good_journey
        
print(best_journey)
    # good_journeys.append(good_journey)
#print(good_journeys)
#print(cow_list)
        
        
        