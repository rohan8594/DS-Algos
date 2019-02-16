# Okta codility challenge


def solution(A, Y):
    # write your code in Python 3.6
    clientTimestamps = {}
    clients = []
    resultMap = {}
    result = []

    for cur in A:
        client = cur.split(' ')[0]
        timestamp = cur.split(' ')[1]

        if client not in clientTimestamps:
            clients.append(client)
            clientTimestamps[client] = list([timestamp])
        else:
            clientTimestamps[client].append(timestamp)

    eachWindowTotals = {}
    for client in clients:
        eachWindowTotals[client] = list()
        curWindow = int(clientTimestamps[client][0]) // 60
        curCount, totalCount = 0, 0
        index = 0

        for curTimestamp in clientTimestamps[client]:
            if int(curTimestamp) // 60 == curWindow:
                if curCount < Y:
                    curCount += 1
            else:
                index = setWindowRequestTotal(index, curWindow, eachWindowTotals,
                                              client, curCount, curTimestamp)

                curWindow = int(curTimestamp) // 60
                totalCount += curCount
                curCount = 1

        index = setWindowRequestTotal(index, curWindow, eachWindowTotals,
                                      client, curCount, curTimestamp)

        totalCount += curCount
        resultMap[client] = totalCount

        index = setWindowRequestTotal(index, curWindow, eachWindowTotals,
                                      client, curCount, curTimestamp)

    # print(eachWindowTotals)
    # print(index)
    for i in range(index):  # index here is total no of windows or minutes in input
        prev5WindowTotal = 0
        for j in range(i, i - 5, -1):
            if j < 0:
                break
            for client in eachWindowTotals.keys():
                if len(eachWindowTotals[client]) - 1 < j:
                    continue
                prev5WindowTotal += eachWindowTotals[client][j]

        if prev5WindowTotal >= 10:
            for client in eachWindowTotals.keys():
                clientTotal = 0
                for j in range(i, i - 5, -1):
                    if j < 0:
                        break
                    if len(eachWindowTotals[client]) - 1 < j:
                        continue
                    clientTotal += eachWindowTotals[client][j]
                if clientTotal / prev5WindowTotal > 0.5:
                    try:
                        eachWindowTotals[client][i + 1] = 0
                    except:
                        pass
                    try:
                        eachWindowTotals[client][i + 2] = 0
                    except:
                        pass

    for client in eachWindowTotals.keys():
        newTotal = 0
        for cur in eachWindowTotals[client]:
            newTotal += cur
        resultMap[client] = newTotal

    for curClient in resultMap.keys():
        result.append(curClient + " " + str(resultMap[curClient]))

    return result


def setWindowRequestTotal(index, curWindow, eachWindowTotals, client, curCount, curTimestamp):
    if index == curWindow:
        eachWindowTotals[client].append(curCount)
        index += 1
    elif index != curWindow and index != int(curTimestamp) // 60:
        for i in range(index, int(curTimestamp) // 60):
            eachWindowTotals[client].append(0)
            index += 1
    elif index == int(curTimestamp) // 60:
        pass
    return index
