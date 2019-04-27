# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite
# restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a
# choice tie between answers, output all of them with no order requirement. You could assume there always
# exists an answer.

# Example 1:

# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

# Note:
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.


class Solution:
    def findRestaurant(self, list1: 'list[str]', list2: 'list[str]') -> 'list[str]':
        placesMap = {}
        minSum = float('inf')
        res = []

        for i, cur in enumerate(list1):
            placesMap[cur] = i

        for i, cur in enumerate(list2):
            if cur in placesMap:
                if (placesMap[cur] + i) < minSum:
                    res = [cur]
                    minSum = placesMap[cur] + i
                elif (placesMap[cur] + i) == minSum:
                    res.append(cur)
        return res
