# coding=UTF-8
# 斐波那契数列.py


def p_fib(n):
    f = [1,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f

def main():
    f = p_fib(10)
    print(f)

main()
