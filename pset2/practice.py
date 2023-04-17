# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 07:44:07 2022

@author: Rowan
"""

# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    f = open(map_filename)
    weighted_edges = []
    lines = f.readlines()
    for line in lines:
        split = line.split(' ')
        edge = WeightedEdge(split[0],split[1],split[2],split[3].strip())
        weighted_edges.append(edge)
        line = f.readline
    f.close()
      
    g = Digraph()
    for edge in weighted_edges:
        if not g.has_node(edge.get_source()):
            g.add_node(edge.get_source())
        if not g.has_node(edge.get_destination()):    
            g.add_node(edge.get_destination())
        g.add_edge(edge)
        
    return g
    print("Loading map from file...")

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
# g = load_map("testing_load_map.txt")
# print(g)


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
# To minimise the total distance travelled between two points. No constraints for the
# first part. Second part has max total travel distance and max outdoor distance as constraints.

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    tmp_path = path[0]
    tmp_length = path[1]
    tmp_outdoor = path[2]
    
    tmp_path = tmp_path + [start]
    #print("current temp path", tmp_path, tmp_length)
    if start == end:
        path[0] = path[0] + [start]
        #print("**COMPLETE PATH**", path)
        return path
    for edge in digraph.get_edges_for_node(start):
        print(edge)
        dest = edge.get_destination()
        total = int(edge.get_total_distance())
        outdoor = int(edge.get_outdoor_distance())
        if dest not in tmp_path: #avoid cycles
            if (best_path == None or (tmp_length + total) <= best_dist) and (tmp_outdoor + outdoor) <= max_dist_outdoors:
                newPath = get_best_path(digraph, dest, end, [tmp_path, tmp_length + total, tmp_outdoor + outdoor], max_dist_outdoors,
                                        best_dist, best_path)
                #print("NEWENEWNEW",newPath)
                if newPath != None:
                    best_path = newPath[0]
                    best_dist = newPath[1]
        #else:
            #print('Already visited', dest)
    return (best_path, best_dist)
    
g = load_map("mit_map.txt")
for edge in g.get_edges_for_node("32"):
    print(edge)
print("FINAL PATH", get_best_path(g,"32","56",[[],0,0],0,0,None))