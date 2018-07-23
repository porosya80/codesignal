def electionsWinners(votes, k):
    winners = 0
    current_winner = max(votes)
    for item in votes:
        if k > 0 and item + k > current_winner:
            winners += 1
        if k == 0 and item == current_winner and votes.count(item) == 1:
            winners += 1
    return winners



votes = [2, 3, 5, 2]
k = 3 
print(electionsWinners(votes, k))
#  = 2
