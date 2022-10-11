n = int(input())
score = [0 for _ in range(300)]
dp = [0 for _ in range(300)]
for i in range(n):
    score[i] = int(input())
    
def initialize():
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0]+score[2], score[1]+score[2])

initialize()

for i in range(3,n):
    dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

print(dp[n-1])
