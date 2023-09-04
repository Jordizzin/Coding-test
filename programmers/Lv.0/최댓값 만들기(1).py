def solution(numbers):
    answer = 0
    numbers.sort()
    # size = len(numbers)
    # answer = numbers[size-2] * numbers[size-1]
    return numbers[-1]*numbers[-2]