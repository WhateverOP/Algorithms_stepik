'''
Первая строка содержит количество предметов 1≤n≤1031≤n≤103 и вместимость рюкзака 0≤W≤2⋅1060≤W≤2⋅106.
Каждая из следующих nn строк задаёт стоимость 0≤ci≤2⋅1060≤ci​≤2⋅106 и объём 0<wi≤2⋅1060<wi​≤2⋅106 предмета (nn, WW, cici​, wiwi​ — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
'''

import numpy as np
import sys

def price_func(some_input):
    N_lines, capacity = np.array(some_input.readline().split()).astype(int)
    table = np.zeros((N_lines,3))
    
    for i in range(0,N_lines):
        table[i][0:2] = np.array(some_input.readline().split()).astype(int)
        table[i][2] = table[i][0]/table[i][1]

    table = np.flip(table[table[:, 2].argsort()], axis=0)

    print(table)
    print(capacity)
    
    price_in_bag = 0
    
    for i in range(0, len(table)):
        N_fits_in_bag = capacity/table[i][1]
        if (N_fits_in_bag >= 1):
            price_in_bag = price_in_bag + table[i][0]
            capacity = capacity - table[i][1]
            table[i][1] = 0
        elif ((N_fits_in_bag < 1) & (N_fits_in_bag != 0)):
            price_in_bag = price_in_bag + N_fits_in_bag*table[i][0]
            capacity = capacity - N_fits_in_bag*table[i][1]
            table[i][1] = table[i][1] - N_fits_in_bag*table[i][1]
        else:
            break
    print(price_in_bag)
    return price_in_bag
    
# test_input = sys.stdin
path_to_text = '/home/opv002/py_notes/git_repos/Algorithms_stepik/Backpack_test.txt'
test_input = open(path_to_text)
price_func(test_input)