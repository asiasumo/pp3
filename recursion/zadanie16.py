def fib():
    a,b = 0,1
    print(a)
    for i in range(1,20):
        a,b = b,a+b
        print(a)
fib()

