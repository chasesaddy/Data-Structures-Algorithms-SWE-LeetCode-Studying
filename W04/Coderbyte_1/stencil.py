from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''
def reverse_str(s: str) -> str:
  # O(n), O()
  stringy = []
  for i in range(len(stringy)-1,-1,-1):
    stringy.append(i)
  return ''.join(stringy)


'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''
def most_freq_substring(s: str, n: int) -> str:
  sub_dict = dict()
  for i in range(len(s)-n+1):
    substring = s[i:i+n]
    if substring in sub_dict:
      sub_dict[substring] += 1
    else:
      sub_dict[substring] = 1
  max_count = max(sub_dict.values())
  final_list = []
  for sub, count in sub_dict.items():
    if count == max_count:
      final_list.append(sub)
  return min(final_list)


'''
What its the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
# @TODO finish -- Have to keep into account the length of the array to know whether to go for the smallest letter or for a letter to get the correct number of index in time. No clue!
def smallest_subsequence(s: str, n: int) -> str:
  if n == 1:
    return min(s)
  elif n >= len(s):
    return s

  sub = ''
  # number of subsequences
  for i in range(n):
    least = float('inf')
    stringy = ''
    indexy = 0
    # loop across string:
    for index, j in enumerate(s):
      if ord(j) < least:
        least = ord(j)
        stringy = j
        indexy = index
    sub += stringy
    s = s[indexy + 1:]
  return sub

def smallest_subsequence_r(s, n):
  if n == 1:
    return min(s)
  elif n >= len(s):
    return s
  else:
    left = smallest_subsequence_r(s[1:], n)
    right = s[0] + smallest_subsequence_r(s[1:], n - 1)
    return min(a, b)


'''
Merge N sorted lists.

Do not just append them all and use .sort()
Think of the merge technique used in mergesort.

Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''
# Other idea: loop around all the arrays at each index. Sort these in a new array?
def merge_n_lists(lst: list[list[int]]) -> list[int]:
  k = len(lsts)
  if k <= 1:
    return lst[0]
  
  mid = k // 2
  lo = lst[:mid]
  hi = lst[mid:]
  left = merge_n_lists(lo)
  right = merge_n_lists(hi)
  # return merge(left, right)

# def merge(left, right):
  p1 = len(left)
  p2 = len(right)
  x = 0
  y = 0
  new_size = p1 + p2
  new_arr = [0] * new_size
  
  while p1 < x and p2 < y:
    if left[p1] <= right[p2]:
      new_arr.append(left[x])
      p1 += 1
    else:
      new_arr.append(right[y])
      p2 += 1
  while p1 < x:
    new_arr.append(left[p1])
    p1 += 1
  while p2 < y:
    new_arr.append(right[p2])
    p2 += 1
  return new_arr


''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''
def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:  
  for i in range(len(lst) - 1):
    most = 0
    track = 0
    while lst[i][0] == lst[i + 1][0]:
      if lst[i][0] > most:
        most = lst[i][0]pirat
        track = i
    lst[i], lst[track] = lst[track], lst[i]

  for i in range(len(lst) - 1):
    least = 0
    track = 0
    while lst[i][1] == lst[i + 1][1]:
      if lst[i][1] < least:
        least = lst[i][1]
        track = i
    lst[i], lst[track] = lst[track], lst[i]
  return lst

def comparison_tuples(lst: list[tuple[int, int]], num: int) -> int:
  if lst[i][1] < lst[i + 1][1]:
    most = lst[i]
  lst[i], lst[i + 1] = most, lst[i]

print(sort_tuples([(1,1), (2,2), (2,1), (1,2)]))
