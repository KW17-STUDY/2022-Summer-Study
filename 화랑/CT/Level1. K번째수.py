def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_arr = sorted(array[i-1:j])
        answer.append(new_arr[k-1])
    return answer