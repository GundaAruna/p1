def add():
    try:
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err1:
        print(err1)
    print(a+b)
add()
