import sys
input = sys.stdin.readline
n, m, h = map(int, input().split())
grid = [[False for _ in range(n+1)] for _ in range(h+1)]