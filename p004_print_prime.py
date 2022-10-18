# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/18/2022 9:50 AM
# 文件名称: p004_print_prime.PY


#再写判断素数的逻辑 只能被1和它本身整除 （也就是被2到它本身的任何一个数能整除就不是素数）
def is_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True

#方法里会有判断素数的逻辑 先写方法名
def print_primes(begin,end):
    for number in range(begin,end+1):
        if is_prime(number):
            print(f"{number} is a prime")



# 做题的时候写的逻辑要做什么
begin = 11
end =25
print_primes(begin,end)