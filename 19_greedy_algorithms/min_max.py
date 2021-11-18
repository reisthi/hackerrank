arr = [4504, 1520, 5857, 4094, 4157, 3902, 822,
       6643, 2422, 7288, 8245, 9948, 2822, 1784,
       7802, 3142, 9739, 5629, 5413, 7232, ]


def solution_one(k, array):
    min_unfairness = max(arr)
    array.sort()
    for i in range(0, len(array)):
        ar = array[i:k + i]
        if len(ar) == k:
            fairness = max(ar) - min(ar)
            if fairness < min_unfairness:
                min_unfairness = fairness
    return min_unfairness


def solution(k, array):
    array.sort()
    return min(array[i:k+1] - array[i] for i in range(0, len(array)))


def test(k, array):
    k = k - 1
    new_array = list()
    array.sort()
    for i in range(len(array) - k):
        print(f"i: {i} i+k: {i+k} array[i]: {array[i]} array[i+k]: {array[i+k]} ===> {array[i+k] - array[i]}")
        new_array.append(array[i+k] - array[i])
    return min(new_array)
