def square_sum(n):
    return sum([i**2 for i in range(1, n+1)])

n = int(input("请输入n的值："))
result = square_sum(n)
print(result)
