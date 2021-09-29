def function_a():
    print("a1")
    # from foo3 import functionB
    print("a2")
    function_b()
    print("a3")


def function_b():
    print("b")
    print("t1")
    print("m1")
    function_a()
    print("m2")
    print("t2")


def c(a_string, size):
    if len(a_string) > 1:
        string_copy = a_string
        while len(string_copy) <= size:
            string_copy += a_string
            if len(string_copy) == size:
                break
        return string_copy[:size].count(a_string[0])
    return size

