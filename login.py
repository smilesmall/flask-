def fibo(x):
    if x == 0:
        resp = 0
    elif x == 1:
        resp = 1
    else:
        return fibo(x-1) + fibo(x-2)
    return resp

assert fibo(5) == 5


print('hello world')


'''
今天是2018年5月31日，测试githup，和linux
今天天气还行 风和日丽
'''
