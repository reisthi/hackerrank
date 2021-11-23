import time
from utils.timer import Timer


def function_a():
    print("a1")
    # from foo2 import functionB
    print("a2")
    function_b()
    print("a3")


def function_b():
    print("b")
    print("t1")


if __name__ == "__main__":
    print("m1")
    function_a()
    print("m2")
    print("t2")


def test(arr, k):
    for i in range(len(arr)-k):
        arr[i+k] - arr[i]


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


def sol(nums, val):
    new_list = [n for i, n in enumerate(nums) if n != val]
    return new_list, len(new_list)


def sol_2(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


def fact(x):
    t = Timer()
    t.start()
    product = 1
    for i in range(x):
        product = product * (i + 1)
    t.stop()
    return product


def fact_recursion(x):
    if x == 0:
        return x
    else:
        return x * fact_recursion(x - 1)




