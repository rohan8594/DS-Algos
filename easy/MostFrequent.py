# Part 1: Given a string with words separated by string, return word that 
#         occurred most frequently. Explain big O runtime of solution.  

# Part 2: Same as above, but return a list of most frequent words. Just 
#         implement a working solution, no need to optimize.

def mostFrequent(s, t):
    
    seen = {}
    
    for curr in s.split(t):
        if curr not in seen:
            seen[curr] = 1
        else:
            seen[curr] += 1
            
    max = seen.keys()[0]
    
    for curr in seen.keys()[1:]:
        if seen[curr] > seen[max]:
            max = curr
    
    return max
    
def mostFrequentList(s, t):
    
    seen = {}
    
    for curr in s.split(t):
        if curr not in seen:
            seen[curr] = 1
        else:
            seen[curr] += 1
            
    max = set()
    max.add(seen.keys()[0])
    
    for curr in seen.keys()[1:]:
        for max_val in max: break
        if seen[curr] > seen[max_val]:
            while(max):
                max.pop()
            max.add(curr)
        elif seen[curr] == seen[max_val]:
            max.add(curr)
        else:
            pass
    
    return list(max)
    
print(mostFrequent("hello-xyz-abc-xyz-xyz-abc-pqr-hello-hello", "-"))
print(mostFrequentList("hello-xyz-abc-xyz-xyz-abc-pqr-hello-hello", "-"))