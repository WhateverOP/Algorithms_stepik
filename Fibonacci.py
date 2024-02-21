def fibonacci(n):
    if n <= 1:
        return n
    else:
        T_arr = []
        T_arr.append(0)
        T_arr.append(1)
        for i in range(2,n):
            T_arr.append(T_arr[i-1] + T_arr[i-2])
        return T_arr[-1] + T_arr[-2]
    
n = int(input())
print(fibonacci(n))