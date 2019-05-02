import sys


def findMidpointCourse_dfs(pairs):
    graph = {u: v for u, v in pairs}
    visited = {u: False for u, v in pairs}
    topoOrder = []

    def dfs(v):
        visited[v] = True
        if graph[v] in visited and not visited[graph[v]]:
            dfs(graph[v])
        topoOrder.append(v)

    for v in visited:
        if not visited[v]:
            dfs(v)

    return topoOrder[::-1][len(topoOrder) // 2]


def findMidpointCourse(pairs):
    # IMPLEMENTATION GOES HERE
    i = 0
    succ = set()
    courseMap = {}

    for pair in pairs:
        succ.add(pair[1])
        courseMap[pair[0]] = pair[1]

    for course in courseMap:
        if course not in succ:
            startCourse = course
            break

    nextCourse = startCourse
    while i < len(pairs) // 2:
        nextCourse = courseMap[nextCourse]
        i += 1

    return nextCourse


s1 = [["CreativeWriting", "Poetry"],
      ["Poetry", "Beowulf"],
      ["Beowulf", "IntroToGerman"]]

s2 = [["DataStructures", "Algorithms"],
      ["FoundationsOfCS", "OperatingSystems"],
      ["ComputerNetworks", "ComputerArchitecture"],
      ["Algorithms", "FoundationsOfCS"],
      ["ComputerArchitecture", "DataStructures"],
      ["SoftwareDesign", "ComputerNetworks"]]

print(findMidpointCourse(s1))
print(findMidpointCourse(s2))
print(findMidpointCourse_dfs(s2))
