# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# Note: Works partially for 24/39 test cases
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: 'List[str]') -> 'List[List[str]]':
        res = []
        wordbuckets = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                genericWord = word[:i] + "_" + word[i+1:]
                wordbuckets[genericWord].append(word)

        # print(wordbuckets)
        deq = collections.deque([(beginWord, 1, [beginWord])])
        visited = {beginWord: True}
        shortest = 0
        while deq:
            curWord, level, curTransform = deq.popleft()

            for i in range(len(curWord)):
                genericWord = curWord[:i] + "_" + curWord[i+1:]
                for word in wordbuckets[genericWord]:

                    if word == endWord and not shortest:
                        shortest = level
                        res.append(curTransform + [word])
                    elif word == endWord and level == shortest:
                        res.append(curTransform + [word])

                    if word not in visited:
                        visited[word] = True
                        deq.append((word, level + 1, curTransform + [word]))
        return res


s = Solution()
s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
