class ComponentNode:
    def __init__(self, numOfLinesChanges):
        self.val = numOfLinesChanges
        self.components = []

    def dfs(self, node):
        speed, count = 0, 0
        if node:
            for child in node.components:
                retval, retcount = self.dfs(child)
                speed += retval
                count += retcount
            return (speed + node.val), (count + 1)
        else:
            return 0, 0

    def getFastestComponent(self, root):
        if not root:
            return None

        maxComp, maxSpeed = None, float('-inf')
        level, nextLevel = [root], []
        while level:
            for node in level:
                if not node.components:
                    continue

                speed, count = self.dfs(node)
                avgSpeed = speed / count
                if avgSpeed > maxSpeed:
                    maxSpeed = avgSpeed
                    maxComp = node.val

                for child in node.components:
                    if child:
                        nextLevel.append(child)
            level = nextLevel
            nextLevel = []
        return maxComp


a = ComponentNode(200)
b = ComponentNode(120)
c = ComponentNode(180)

a.components.append(b)
a.components.append(c)

d = ComponentNode(110)
e = ComponentNode(20)
f = ComponentNode(30)
g = ComponentNode(150)
h = ComponentNode(80)

b.components.append(d)
b.components.append(e)
b.components.append(f)

c.components.append(g)
c.components.append(h)


print(a.getFastestComponent(a))
