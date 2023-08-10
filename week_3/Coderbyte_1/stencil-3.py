from __future__ import annotations

'''
Return the list of numbers as a string separated by space using recursion
'''
def recurse(lst: list[int]) -> None:
  if lst == []:
    return ""
  return recurse(lst[:-1]) + str(lst[-1]) + " "

'''
2. Calculate the factorial of N iteratively and recursively
'''
def fact_iter(n: int) -> int:
  output = 1
  for k in range(2,n+1):
    output *= k
  return output

def fact_recursive(n: int) -> int:
  if n == 1:
    return 1
  return fact_recursive(n - 1) * n
    

'''
3. Use binary search to find the index of a list that a certain number exists at. 
Return -1 if number does not exist. Assume that the list is sorted.
'''
def find_index(lst: list[int], val: int) -> int:
  pass


'''
4. Use binary search to find the index of a list that is the 
biggest number less than or equal to the given value. 
Return -1 if such a number does not exist. Assume that the list is sorted.
'''
def find_closest(lst: list[int], val: int) -> int:
  pass
