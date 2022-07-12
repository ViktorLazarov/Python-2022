def sum_nums(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum


print(sum_nums(2, 3, 4, 5, 6, 435))
