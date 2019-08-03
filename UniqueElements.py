# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique(s):
  a = []
  for i in s:
    if i not in a:
      a.append(i)
    else:
      pass
  return a

print (unique([1,2,3,3,3,3,4,5]))