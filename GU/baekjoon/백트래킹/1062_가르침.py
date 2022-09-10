import sys
from itertools import combinations

input = sys.stdin.readline
n, k = map(int, input().split())
antic = set(['a', 'n', 't', 'i', 'c'])
words = [input().rstrip()[4:-4] for _ in range(n)]
remain_alpha = set([chr(i) for i in range(97, 123)])-antic
learn_alpha = [False for _ in range(26)]
max_cnt = 0

def check():
    learnable = 0
    for word in words:
        for w in word:
            if not learn_alpha[ord(w)-97]:
                break
        else:
            learnable += 1
    return learnable
if k < 5:
    print(max_cnt)
else:
    for i in antic:
        learn_alpha[ord(i)-97] = True

    for teach in combinations(remain_alpha, k-5):
        for t in teach:
            learn_alpha[ord(t)-97] = True

        cnt = check()
        max_cnt = max(max_cnt, cnt)

        for t in teach:
            learn_alpha[ord(t)-97] = False

    print(max_cnt)
    '''
    1. ord가 너무 많이 들어가면 시간초과 난다.
        이에 ord(i)-ord('a') 말고 ord(i)-97 넣었더니 잘 된다!
    2. 처음에 brute force하게 풀었는데 안됨..!
        모든 알파벳에서 k개를 뽑았었는데 
        a n t i c는 무조건 배우는 알파벳이라 
        26개의 알파벳에서 k개를 뽑는게 아닌
        21개의 알파벳에서 k-5개를 뽑는 방법으로 해결!
    3. 일반적으로 dfs로 조합을 뽑는 것 보단 
        combinations를 쓰는 것이 더 빠르게 작용한다.
    '''