'''
Пусть a >= b > 0 и r = a % b (остаток от деления a на b)
Тогда НОД(a, b) = НОД(r, b)
'''

def gcd(a, b):
    if (a == 0): return b
    elif (b == 0): return a
    elif (a >= b): return gcd(a % b,b)
    elif (a <= b): return gcd(a, b % a)

a, b = map(int, input().split())
print(gcd(a, b))