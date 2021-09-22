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
