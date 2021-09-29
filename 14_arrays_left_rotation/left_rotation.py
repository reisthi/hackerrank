def solution(array, rotations):
    """ Send the first item in the array to the back of the array on each iteration. """
    for item in range(0, rotations):
        first = array.pop(0)
        array.append(first)
    return array
