def solution(cost, money):
    h = dict()

    # add items to a hashtable
    for i, item in enumerate(cost):
        h[item] = i

    for i in range(len(cost)):
        comp = money - cost[i]
        if comp in h and h[comp] != i:  # make lookups
            print(i + 1, h[comp] + 1)
            break


# STDIN       Function
# -----       --------
# 2           t = 2
# 4           money = 4
# 5           cost[] size n = 5
# 1 4 5 3 2   cost = [1, 4, 5, 3, 2]
# 4           money = 4
# 4           cost[] size n = 4
# 2 2 4 3     cost = [2, 2, 4, 3]


# Complexity Analysis
#
# Time complexity: O(n)O(n). We traverse the list containing nn elements exactly twice.
# Since the hash table reduces the lookup time to O(1)O(1), the overall time complexity is O(n)O(n).
#
# Space complexity: O(n)O(n).
# The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.
