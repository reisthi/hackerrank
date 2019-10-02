st = 'ABCDCDC'
sub_st = 'CDC'


def count_sub_string(str, sub_str):
    


len_sub = len(sub_st)
counter = 0
for a in range(len(st)):
  if a <= (len(st) - len_sub):
    print(st[a:a + len_sub])
    if sub_st in st[a:a + len_sub]:
      counter += 1

print(counter)