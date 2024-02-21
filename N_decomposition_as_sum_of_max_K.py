'''
По данному числу 1≤n≤1091≤n≤109 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.
'''

import numpy as np
import sys

def natural_series_upper_limit(x):
    return 1/((np.sqrt(1 + 8*x) + 1)/(4*x))

def find_max(some_input):
    x = int(some_input.readline())
    # print(f'x = {x}')
    n = natural_series_upper_limit(x)
    # print(f'n  = {n}')
    if (n % int(n) == 0):
        n = int(n)
        numbers = np.arange(1, n+1).astype(int)
        print(len(numbers))
        print(' '.join([str(i) for i in numbers]))
    else:
        n = int(n)
        numbers = np.arange(1, n+1).astype(int)
        while (numbers.sum() != x):
            numbers[-1] = numbers[-1] + 1
        print(len(numbers))
        print(' '.join([str(i) for i in numbers]))

def find_max_2(some_input):
    x = int(some_input.readline())
    natural_series = []
    numbers = []
    i = 0
    j = 1
    sum_numbers = 0
    while sum_numbers != x:
        natural_series.append(j)
        if sum_numbers < x:
            numbers.append(natural_series[i])
            sum_numbers += numbers[-1]
            i += 1
        else:
            last = numbers.pop()
            prev_last = numbers.pop()
            numbers.append(last)
            sum_numbers = sum_numbers - prev_last
        j += 1
    print(len(numbers))
    print(' '.join([str(i) for i in numbers]))
        
test_input = sys.stdin
# find_max(test_input)
find_max_2(test_input)