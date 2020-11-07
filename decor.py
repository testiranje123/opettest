import time


def log(func):
    def inner(*args,**kwargs):
        a= time.time()
        print("pocetak funckije u ",a)
        func(*args,**kwargs)
        b=time.time()
        print("kraj funckije u ", b)
        print("ukupno je: ", b-a)
    return inner

@log
def run_time(tim):
    c=0
    for i in range(1,tim):
        c+=i^2+i*10+3

run_time(50000000)
