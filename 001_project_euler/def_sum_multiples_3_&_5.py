# sum of multiples of 3 & 5

def sum_divisible_by(k, n):
    p = (n - 1) // k
    return k * p * (p + 1) // 2


def sum_multiples_3_and_5(n):
    """
    :param n: upper bound
    :return:
    """
    return sum_divisible_by(3, n) + sum_divisible_by(5, n) - sum_divisible_by(15, n)


print(sum_multiples_3_and_5(10))  # output: 23
print(sum_multiples_3_and_5(100))  # output: 2318
print(sum_multiples_3_and_5(1_000))  # output: 233168
print(sum_multiples_3_and_5(10_000))  # output: 23331668
print(sum_multiples_3_and_5(100_000))  # output: 2333316668
print(sum_multiples_3_and_5(1_000_000))  # output: 233333166668
