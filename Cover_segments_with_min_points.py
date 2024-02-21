'''
По данным nn отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤1001≤n≤100 отрезков.
Каждая из последующих nn строк содержит по два числа 0≤l≤r≤1090≤l≤r≤109, задающих начало и конец отрезка.
Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек несколько, выведите любое из них.
'''

import numpy as np
import sys

def cover(some_input):
    N_lines = int(some_input.readline())
    table = []

    for i in range(0,N_lines):
        table.append(some_input.readline().split())

    table = np.array(table).astype(int)
    table = table[table[:, 1].argsort()]

    # print(table)
    
    points = []
    points.append(table[0][1])

    # print(points)
    
    for i in range(1,len(table)):
        if ((points[-1] >= table[i][0]) & (points[-1] <= table[i][1])):
            continue
        else:
            points.append(table[i][1])
            
    print(len(points))
    print(' '.join([str(i) for i in points]))
    
# test_input = sys.stdin
path_to_text = '/home/opv002/py_notes/git_repos/Algorithms_stepik/Cover_segments_with_min_points_test.txt'
test_input = open(path_to_text)
cover(test_input)