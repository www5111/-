def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1到100之间的素数有:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")


def fibonacci(n):
    """生成斐波那契数列前n项"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

fib_sequence = fibonacci(20)
print("斐波那契数列前20项:")
print(fib_sequence)


total = 0
num = 1

while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print("1-10000之间能被3或5整除但不能被15整除的数的和为:", total)