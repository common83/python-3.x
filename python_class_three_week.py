import  sys

def digit():
    z = 1.23e-4 + 5.6e+89j
    print("real",z.real)
    print("imag",z.imag)

    x = 4.5
    y = 4
    print("int",int(x))
    print("float",float(y))
    print("complex",complex(y))

    print("type",type(x),type(y),type(z))

def string_operator():
    str1 = "Hello"
    str2 = 'John'
    greeting = "Hello World"
    x = 7

    print("type",type(str1))
    print("str index", greeting[0], greeting[x-1])
    print("str revert index", greeting[-1], greeting[-2])
    print("sub str by index", greeting[0:x-2])
    print("+ combine str", str1 + str2)
    print("* repeat str", 3 * str1)

    print("str convert type", str(123), str(123.456), str(123e+10))

# month.py
def month():
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    n=input("请输入月份数(1-12):")
    pos=(int(n)-1) * 3
    monthAbbrev=months[pos:pos+3]
    print("月份简写是"+monthAbbrev+".")


def tuple_test():
    t1 = 123, 12.3, ("hello", "中国")
    t2 = 2, 3, 4, 5

    print("index tuple",t1[1],t1[2:])
    print("index tuple",t1+t2, 3*t2)

#string_operator()
tuple_test()