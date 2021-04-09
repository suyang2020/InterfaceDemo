import requests

data = {
    "bankSerialNumber": "123456711111111111111",
    "bankCode": "0051",
    "cardType": 1,
    "backgroupColor": "1",
    "cardTechnology": 1,
    "cardSubject": 1,
    "cardTypography": 1
    }

files = {"facadeImage": ('1075,686.jpg', open('E:\\hengbao\\DIY银行卡\\case\\测试文件\\横版\\1075,686.jpg', "rb"), 'image/jpeg', {})}
url = "https://cp.hengbao.net.cn:9010/pos/order/submitOrder"

# res = requests.post(url=url, data=data, files=files).text

# print(res)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkTable:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            pass

from selenium.webdriver.support import expected_conditions as EC


def dec(f):
    n = 3

    def wrapper(*args, **kw):
        return f(*args, **kw) * n

    return wrapper


@dec
def foo(n):
    return n * 2

foo(2)

#
# def adder(x):
#     def wrapper(y):
#         return x + y
#     return wrapper
#
#
# adder5 = adder(5)
# print(adder5(adder5(6)))


def w1():
    print('正在装饰')

    def inner():
        print('正在验证权限')

    return inner()


class SingleExceple(object):
    is_single = None
    is_init = False

    def __new__(cls, *args, **kwargs):
        if cls.is_single is None:
            cls.is_single = super.__new__(cls)
            return cls.is_single

    def __init__(self):
        if not SingleExceple.is_init:
            return
        print("初始化")
        SingleExceple.is_init = True


def remove_dup(s):
    l = list(s)
    n = len(l)

    for i in range(n-1):
        if l[i] == l[i+1]:
            l.remove(l[i])
        else:
            pass


remove_dup("111223")



