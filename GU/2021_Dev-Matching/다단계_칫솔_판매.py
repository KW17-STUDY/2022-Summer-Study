from collections import defaultdict
from math import ceil

def recursive(seller, money, money_list):
    global tree
    if money*0.1 < 1:
        money_list[seller] += money
        return
    mine, yours = int(ceil(money * 0.9)), money - int(ceil(money*0.9))
    money_list[seller] += mine     
    recursive(tree[seller], yours, money_list)
    return
    
def solution(enroll, referral, seller, amount):
    global tree
    
    answer = []
    tree = defaultdict(str)
    money_list = defaultdict(int)
    
    # tree만들기 -> 자식: 부모
    for i in range(len(enroll)):
        #부모가 없다면 다음 user로 넘어가기
        if referral[i] == '-': 
            continue
        tree[enroll[i]]=referral[i]

    # seller에 사용자가 2번 들어갈 수 있으므로 차례대로 하나씩 받아주기
    for a_seller, sell_amount in zip(seller, amount):
        recursive(a_seller, sell_amount*100, money_list)

    for user in enroll:
        answer.append(money_list[user])
    
    return answer

'''
#Remind
1. 문제를 잘 읽자.
문제에서 seller안에 중복된 사용자가 들어갈 수 있다고 했는데 고려하지 않아서 틀려 시간을 많이썼다.

'''