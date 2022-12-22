
# yield可以理解为一个return操作，但是和return又有很大区别，执行完return，当前函数就终止了，函数内部的所有数据，所占的内存空间，全部都没有了
# yield在返回数据的同时，还保存了当前的执行内容，当你再一次调用这个函数时，会找到在此函数中的yield关键字，然后从yield的写一句开始执行

def num_print():
    print('yield_1')
    yield 'yield_1 return'
    print('yield_2')
    yield 'yield_2 return'
    print('yield_3')
    yield 'yield_3 return'
    print('yield_4')
    yield 'yield_4 return'

#for i in num_print():
#    print('i:',i)

o = num_print()

next(o)
next(o)
next(o)
next(o)