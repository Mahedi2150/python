def fibo(x):
    f = 0
    s = 1
    print(0)
    print(1)
    for i in range(2,x):
        fi = f+s
        f = s
        s = fi
        print(fi)

fibo(10)