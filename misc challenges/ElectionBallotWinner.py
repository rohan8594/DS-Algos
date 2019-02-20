# Complete the electionWinner function below.
def electionWinner(votes):
    vote_count = {}

    for vote in votes:
        if vote not in vote_count:
            vote_count[vote] = 1
        else:
            vote_count[vote] += 1

    max_votes = getCandidatesWithMostVotes(vote_count)

    result = max_votes[0]
    for cur in max_votes[1:]:
        if cur > result:
            result = cur

    return result


def getCandidatesWithMostVotes(vote_count):
    for first in vote_count:
        break
    max_votes = [first]

    for curKey in vote_count.keys():
        max = max_votes[0]
        if vote_count[curKey] > vote_count[max]:
            while(max_votes):
                max_votes.pop()
            max_votes.append(curKey)
        elif vote_count[curKey] == vote_count[max]:
            if curKey != max:
                max_votes.append(curKey)
    return max_votes
