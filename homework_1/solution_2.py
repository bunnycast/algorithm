def solution(numbers):
    sum = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum.append(numbers[i] + numbers[j])
    set_sum = set(sum)
    answer = sorted(list(set_sum))
    return