def max_no(l):
  maximum_no=l[0]
  for i in lst:
    if i>maximum_no:
      maximum_no=i
  return maximum_no


def min_no(lst):
  min_num=lst[0]
  for i in lst:
    if i<min_num:
      min_num=i
  return min_num
  
lst=[7,6,2,12,34,78]
print(max_no(lst))
print(min_no(lst))