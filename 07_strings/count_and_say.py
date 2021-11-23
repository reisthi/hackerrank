# Given a positive integer n, return the nth term of the count-and-say sequence.
#
# Example 1:
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

def solution(n) -> str:
    if n <= 1:
        return '1'

    s = '1'

    for i in range(n - 1):
        previous, count = s[0], 0
        new = ''

        for current in s:
            if previous != current:
                new += str(count) + previous
                previous, count = current, 1

            else:
                count += 1

        new += str(count) + previous
        s = new
    return s