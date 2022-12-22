
# python对协程的支持是通过generator生成器实现的

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

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)# 1、 首先调用c.send(None)启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

#注意到consumer函数是一个generator，把一个consumer传入produce后：

#首先调用c.send(None)启动生成器；

#然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

#consumer通过yield拿到消息，处理，又通过yield把结果传回；

#produce拿到consumer处理的结果，继续生产下一条消息；

#produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。




























