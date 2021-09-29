import random
from timeit import default_timer as timer


def gen_random_list(n, mini, maxi):
    a_list = list()
    [a_list.append(random.randint(mini, maxi)) for a in range(0, n)]
    return a_list


def a_timer():
    start = timer()
    end = timer()
    print(f"Finished: {end - start} ms")
