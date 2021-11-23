st = 'ABCDCDC'
sub_st = 'CDC'


def count_sub_string(string, sub_string):
    counter = 0
    len_sub_string = len(sub_string)

    # iterate entire str
    for x in range(len(string)):
        # prevent index errors
        if x <= (len(string) - len_sub_string):
            if sub_string in string[x:x + len_sub_string]:
                counter += 1
    return counter


def cc(string, sub_string):
    counter = 0
    string_to_be_tested = string
    x = 0

    for i in range(len(string)):
        if i <= (len(string) - len(sub_string)):
            if string_to_be_tested[i] == sub_string[x]:
                x += 1
                if sub_string in string_to_be_tested:
                    counter += 1
        string_to_be_tested = string_to_be_tested[1:]
    return counter


def solution(string, substring):
    counter = 0

    for item in range(0, len(string)):
        if string[item:len(substring)] == substring:
            counter += 1

    return counter
