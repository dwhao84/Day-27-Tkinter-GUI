
# 運用unlimited Arguments去計算數字的總和。
def add(*args):
    sum = 0
    for n in args:
        sum += n
    
    print((f"sum: {sum}"))
    return sum

add(1, 4, 5, 6, 7)

def calculate(n, **kwargs):
    # for (key, value) in kwargs.items():
    #     print(f"key: {key}")
    #     print(f"value: {value}")
    # print(f"kwargs: {kwargs}")
    # print(kwargs["add"]) # 找到kwargs add的value。
    #
    # 用n來坐數字的計算。
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"找到n的結果：{n}")
    
calculate(2, add=3, multiply=5)