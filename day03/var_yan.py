# 声明一个全局变量
# 在方法类对全巨变量重新赋值，需要加global，引入全局变量
a='你好中国中国'
def b_1():
    print(a)
    b='kkljjjjl'
def b_2():
    global  a
    a='你好世界哈哈哈'
    print(a)
    print(b_1)
if __name__ == '__main__':
    b_1()
    b_2()
    b_1()