#6
t = int(input())
for _ in range(t):
    num = int(input())
    dp = [0 for _ in range(num+1)]
    dp[0] = 1
    materials = [1,2,3]

    for i in range(1, num+1):
        for material in materials:
            if i-material >= 0:
                dp[i] += dp[i-material]
    
    print(dp[-1])



'''
순서를 신경쓰지 않고 뽑은 경우
#6
t = int(input())
for _ in range(t):
    num = int(input())
    dp = [0 for _ in range(num+1)]
    dp[0] = 1
    materials = [1,2,3]

    for material in materials:
        for i in range(1, num+1):
            if i-material >= 0:
                dp[i] += dp[i-material]
    
    print(dp[-1])
'''