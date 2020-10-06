# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the
# itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
# order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical
# order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.

# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

# LOGIC: The nice thing about DFS is it tries a path, and if that's wrong (i.e. path does not lead to
#        solution), DFS goes one step back and tries another path. It continues to do so until we've
#        found the correct path (which leads to the solution). You need to always bear this nice feature
#        in mind when utilizing DFS to solve problems.
#
#        In this problem, the path we are going to find is an itinerary which:
#        1. uses all tickets to travel among airports
#        2. preferably in ascending lexical order of airport code

# NOTE: Refer to leetcode discussions for more thorough explanation

import collections


class Solution:
    def findItinerary(self, tickets: 'list[list[str]]') -> 'list[str]':
        airportMap = collections.defaultdict(list)
        itenary = []

        for a, b in sorted(tickets)[::-1]:
            airportMap[a].append(b)

        def visit(airport):
            while airportMap[airport]:
                visit(airportMap[airport].pop())
            itenary.append(airport)

        visit('JFK')
        return itenary[::-1]
