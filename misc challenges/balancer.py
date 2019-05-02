import random


class Balancer:
    def __init__(self, weights):
        self.weights = weights
        self.total = sum([weight[1] for weight in weights])
        match_list = []
        for weight in self.weights:
            for i in range(0, weight[1]):
                match_list.append(weight[0])
        self.match_list = match_list

    def request(self):
        balancer = random.randint(0, self.total-1)
        return self.match_list[balancer]


# b = solution.Balancer([['a', 1], ['b', 1], ['c', 8]])
# matches = {'a': 0, 'b': 0, 'c': 0}
# for i in range(20000):
#     matches[b.request()] += 1
# print(matches)
