def solve(num):
    a = 0
    c = num
    while num > 0:
        r = num % 10
        num = num // 10
        a = (10 * a) + r
    if a == c:
        return True
    else:
        return False
num = 25352
print(solve(num))