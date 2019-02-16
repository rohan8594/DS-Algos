def getDay(day, n):
    days = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
    
    n = n % 7
    
    newDay = (days[day] + n) % 7
    
    for key, val in days.items():
        if newDay == val:
            return key
            
print(getDay('Sat', 23))
