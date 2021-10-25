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
