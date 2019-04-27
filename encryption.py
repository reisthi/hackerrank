import math
import os


# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ', '')  # remove white spaces
    square_root = math.sqrt(len(s))  # get square root
    cols = math.ceil(square_root) # define columns
    rows = math.floor(square_root) # define rows
    if cols * rows < len(s):
        rows = math.ceil(square_root)  # ensure  cols * rows >= length of s

    a_list = list()
    for a in range(int(rows)):
        sub_list = list(s[:cols])
        a_list.append(sub_list)
        s = s[cols:]

    r = len(max(a_list, key=len))
    all_elements = [sum([x[i:i + 1] for x in a_list], []) for i in range(r)]
    another_list = list()
    for a in all_elements:
        another_list.append(''.join(a))
    return str(' '.join(another_list))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
