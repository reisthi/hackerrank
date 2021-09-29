def s(array):
    jumps, current_index = 0, 0
    for op in range(0, (len(array) - 2)):
        if op == current_index:
            if current_index <= len(array):
                if array[op + 1] == 0 and array[op + 2] == 0:
                    jumps += 1
                    current_index += 2
                elif array[op + 1] == 0:
                    jumps += 1
                    current_index += 1
                else:
                    jumps += 1
                    current_index += 1
    return jumps
