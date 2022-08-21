#33~05
from itertools import combinations, permutations
import sys


def rmStartTeamParticipants(st_team):
    participants = [i for i in range(1,n+1)]
    for s in st_team:
        if s in participants:
            participants.remove(s)
    return participants[:]
n = int(input())
input = sys.stdin.readline
grid = [list(map(int,input().split())) for _ in range(n)]
start_team, link_team = [], []
INF = sys.maxsize
min = INF
comb = list(combinations([i for i in range(1,n+1)], int(n//2)))
for i in range(len(comb)//2):
    start_score, link_score = 0, 0
    start_team = list(comb[i])
    link_team = rmStartTeamParticipants(start_team)
    for pair in permutations(start_team, 2):
        start_score += grid[pair[0]-1][pair[1]-1]
    for pair in permutations(link_team, 2):
        link_score += grid[pair[0]-1][pair[1]-1]
    
    diff = abs(start_score - link_score)
    if min > diff:
        min = diff
    
print(min)
    



