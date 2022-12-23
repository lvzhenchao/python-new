
# 序列指的是可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们
# 包括：字符串、列表、元组、集合、字典

# 列表：所有元素都放在一对中括号里面，相邻元素之间用逗号分隔；列表可以存储任何类型的数据

list1 = ['吕振超', 1, [2,3,4], 3.0]
print(type(list1))

# 创建列表
# 1、[]直接创建
listname = ['列表']
# 2、使用list()函数创建
list2 = list("内置函数创建列表")
print(list2)
print(type(list2))

## list()函数可以将其它数据类型转换为列表类型
# 将字符串转换列表
list3 = list("hello")
print(list3)
# 将元组转为列表
tuple = ('python', 'java', 'c++')
list4 = list(tuple)
print(list4)
# 将字典转为列表
dic = {'a': 100, 'b':23}
list5 = list(dic)
print(list5)

## 列表添加元素
### append() 追加
l = ['java','python']
l.append('php')
print(l)
### extend方法
l.extend('c')
print(l)
### insert()可以在列表中间某个位置插入元素
l.insert(1,'golang')
print(l)

















