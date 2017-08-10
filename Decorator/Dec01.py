#coding:utf-8
#Author:TonyHu

def log_cost_time(func):
    def wrapper(*args,**kwargs):
        import time
        begin = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            print('func %s cost %s'%(func.__name__,time.time()-begin))
    return wrapper

@log_cost_time
def complex_func(num):
    ret = 0
    for i in range(num):
        ret += i*i
    return ret

if __name__ == '__main__':
    print(complex_func(100000))

