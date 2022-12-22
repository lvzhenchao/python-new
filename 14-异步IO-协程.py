
# 协程优势
## 1、极高的执行效率，因为子程序切换不是线程切换，而是程序自身控制，没有线程切换的开销
## 2、不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了

## 生成器
L = [x * x for x in range(10)]
print(L)

### 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()
g = (x * x for x in range(10))
print(g)
### 要打印出生成器的元素，可以通过next()函数
### generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

### 在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
	
o = odd()
next(o)
next(o)
next(o)




























