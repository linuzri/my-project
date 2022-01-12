globalvar = 10

def read():
    print(globalvar)
def write1():
    global globalvar
    globalvar = 5
def write2():
    globalvar = 15


read()
write1()
read()
write2()
read()