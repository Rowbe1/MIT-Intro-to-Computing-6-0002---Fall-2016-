# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:30:58 2022

@author: Rowan
"""

# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

import unittest

#
# A set of data structures to represent graphs
#

class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # This function is necessary so that Nodes can be used as
        # keys in a dictionary, even though Nodes are mutable
        return self.name.__hash__()


class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, total_distance, outdoor_distance):
        Edge.__init__(self,src,dest)
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance

    def get_total_distance(self):
        return self.total_distance

    def get_outdoor_distance(self):
        return self.outdoor_distance

    def __str__(self):
        return str(self.src)+"->"+str(self.dest)+\
            " (" + str(self.total_distance) +\
                ", " + str(self.outdoor_distance) +")"


class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dict of Node -> list of edges

    def __str__(self):
        edge_strs = []
        for edges in self.edges.values():
            for edge in edges:
                edge_strs.append(str(edge))
        edge_strs = sorted(edge_strs)  # sort alphabetically
        return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

    def get_edges_for_node(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        if node in self.nodes:
            raise ValueError("node in graph")
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def add_edge(self, edge):
        """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the  graph."""
        src = edge.get_source()
        dest = edge.get_destination()
        total = edge.get_total_distance()
        outdoor = edge.get_outdoor_distance()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("node not in graph")
        else:
            self.edges[src].append(dest)
            self.edges[src].append(total)
            self.edges[src].append(outdoor)


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

g = Digraph()
na = Node('a')
nb = Node('b')
nc = Node('c')
g.add_node(na)
g.add_node(nb)
g.add_node(nc)
e1 = WeightedEdge(na, nb, 15, 10)
e2 = WeightedEdge(na, nc, 14, 6)
e3 = WeightedEdge(nb, nc, 3, 1)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)

print(g)
print(g.get_edges_for_node(na))
print(g.get_edges_for_node(nb))
print(g.get_edges_for_node(nc))