# Strings, Sorting Algorithms

##  Free Response Questions

###  Strings

#### 1. What is a string? How is a string created in memory?

-   A sequence of characters.
-   Core data type in most languages. I believe a string has to be UTF8. That probably doesn't include every language.

String is created in memory as an array of characters.



#### 2. How can we calculate the frequencies of each character in a string?

Make an array/list to cover all the unicode characters. Each value will represent that character's unicode code

1. Instantiate an empty dict

2. Loop through the string

3. if the character is already in the dictionary add 1 more to it.

4. if the character isn't in the dictionary, create a key of current character at value of 1.

5. After loop, return dictionary

Code example:

```

def freq(s):

my_dict = dict()

for c in s:

if c in my_dict:

my_dict[c] += 1

else:

my_dict[c] = 1

return my_dict

```



#### 3. What is an anagram? How can we check if 2 strings are an anagram?

An anagram is a string of characters that when rearranged is the same as another string of characters. Check if 2 strings are anagrams by:

-   Checking the frequency of characters
    
-   Sorting the characters
    

Time: O(n)
Space: O(1)
Can also sort them and compare, but that would be worse time complexity at O(n log n)



#### 4. What are 2 ways to determine if a string is a palindrome?

The string and a reverse of it should be equal.

Have pointers at head going forward and at tail going backward. Both one character at a time. The characters should be the same at each interval.  
  

Wouldn’t you be able to conclude this when they overtake one another half way thru? At that point they should have been equal up to that point



#### 5. What is the runtime to concatenate a string with a character?

O(n). Strings are immutable. A copy of the string has to be made, aka `n` length before the character is added to the string. Actually the concatenated character has runtime as well. So specifically it would be O(n+c) right or am i still missing this? This would be for runtime and space.



#### 6. What is the difference between substring vs. subsequence?

Substring is a sequence of consecutive characters in a string. A subsequence is a sequence of characters that don't have to be consecutive



#### 7. Let s = 'coachable rocks'​. Can you give an example of a subsequence of s that is not a substring s? What about a substring that is not a subsequence?

A subsequence that is not a substring is che. All substrings are subsequences

Example subsequence: cbr

Example substring: able




###  Sorting

#### 1. What does it mean to sort an array?

Having all the elements in some ascending or descending order based on some comparison.



#### 2. How does sorting work for strings?

Check the `ord` or unicode value of each character. Arrange these in ascending or descending numerical order.



#### 3. What do you need to do if you are sorting objects? How is it different from strings, integers, etc?

Objects aren't inherently greater or less than any other objects. A comparison has to be coded to determine what logic should be used for object. Objects are about abstraction so they will include different data types. While integers, floats, strings, bool all are compared based on their values. Objects don't have one value.

For objects some comparison methods are: __lt__, __le__, __gt__, __ge__, __len__, __eq__



#### 4. Describe how selection sort works and its runtime and space complexity

Selection sort compares each value starting from the head with the rest of the remaining elements to the right to find the smallest value and swap it to its place at the front. The same process is repeated for each value to the right and only checking for lowest value with remaining values to the right.

Runtime: O(n^2). Nested loops going through the entire length

Space: O(1)



#### 5. Describe how insertion sort works and its runtime and space complexity

Insertion sort works by being partially sorted to the left. The integer to the immediate right of the sorted side gets sorted. This means the integer moves X amount of spots to the left and X amount of sorted integers move to the right.

Runtime: O(n^2). Nested full loops.

Space: O(1)



#### 6. Describe how merge sort works and its runtime and space complexity

Merge sort splits the array into two halves again and again until each split is 1 element. If the size is odd then at the end some elements will be size 2. Then two elements are merged together and sorted. This continues until there are two halves left and one more merge and sort to have the sorted array. Merge sort is not done in place like the other sort algorithms. It requires an additional array of size n.

If array a bigger size than 2 like 11 then: Split starts at 5 arrays vs 6 arrays. The 5 array side will eventually have some elements of size 2

Runtime: O(n log n) log n comes from the dividing in two part. n comes from the needing to merge n length elements together. Bit worse than quick sort.

Space: O(n) sorted copy of the array



#### 7. Describe how quick sort works and its runtime and space complexity

Quick sort starts with a random pivot element to partition the array. Items that are smaller than the pivot are placed on the left side while items that are greater are placed on the right side. Then the two sides are each sorted which makes the whole array sorted.

Runtime: O(n log n) usually and best case. O(n^2) in a rare worst case. This is why shuffling is important. Bit better than merge sort on average

Space: O(log n) is average using stack to store items that need to be sorted. O(n) is worst when the split is size 0 and length n - 1.



#### 8. Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could have been the pivot element in a previous iteration?

2 or 3. The pivot could only happen once. Both numbers have smaller numbers to the left and higher numbers to the right.



#### 9. What's different between quicksort and mergesort? What are the tradeoffs between the two?

The common part is they are both divide and conquer algos. Merge sort immediately divides the array into more and more subarrays. While quick sort has a pivot element that partitions the array into two equal or unequal sides, left smaller than and right greater than the pivot. Then the two sides are sorted while merge sort keeps merging subarrays the size of 1 with another sub array until it's all merged.
- Quick sort has a better average run time and is usually the fastest sort algo.

- Merge sort is always O(n log n)

- Quick sort space complexity only uses O(log n) usually but could be O(n) in rare cases. Merge sort is always O(n)



#### 10. What does divide and conquer mean? Which sorting algorithms use this approach?

Merge sort, quick sort, and heap sort use divide and conquer. Divide part means the array is divided into smaller sub-arrays. Then the conquer part is the sub-arrays are merged and sorted with one another.



#### 11. What is the difference between 3-way quicksort and standard quicksort?

3-way quicksort makes a separate third sub array of all the pivots. While standard puts the equal value to pivots on either side. Not its own section.



#### 12. Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster here?

3-way quicksort is better when there aren't many different values or if there are a lot of duplicates. Not sure how the pivot or integer with the most duplicates would be identified.



#### 13. Suppose you have an array with only 5 distinct elements (only the numbers 1-5).

##### a. What is the worst-case runtime of quicksort? Why?

-   O(n^2)
-   When the pivot is 1 or 5. 
-   All the values go to one of the two splits. That doesn’t provide any log n speed gains.

##### b. What is the worst-case runtime of 3-way quicksort? Why?

-   O(n log n)
-   first split could be [1,2] [3] [4,5]
-   For best case runtime:
-   The one distinct element will be picked as the middle pivot value. The left and right splits will both have nothing in them. That's O(3 or 4) (cuz of the partitions).



##  Trace Sorting Algorithms

### Trace out all the intermediate steps on the string "COACHABLEROCKS"​ for each of the following sorting algorithms. You don't need to include every swap, but you should include the most important intermediate steps.

1.  #### Insertion Sort

C O A C H A B L E R O C K S

C O A C H A B L E R O C K S

A C O C H A B L E R O C K S

A C C O H A B L E R O C K S

A C C H O A B L E R O C K S

A A C C H O B L E R O C K S

A A B C C H O L E R O C K S

A A B C C H L O E R O C K S

A A B C C E H L O R O C K S

A A B C C E H L O R O C K S

A A B C C E H L O O R C K S

A A B C C C E H L O O R K S

A A B C C C E H K L O O R S

A A B C C C E H K L O O R S



2.  #### Selection Sort

A O A C H C B L E R O C K S

A B A C H C O L E R O C K S

A A B C H C O L E R O C K S

A A B C H C O L E R O C K S

A A B C C H O L E R O C K S

A A B C C H C L E R O O K S

A A B C C H C E L R O O K S

A A B C C H C E K R O O L S

A A B C C H C E K L O O R S

A A B C C H C E K L O O R S

A A B C C H C E K L O O R S

A A B C C H C E K L O O R S

A A B C C H C E K L O O R S



3.  #### Quicksort (No Shuffle)

C O A C H A B L E R O C K S

K is pivot. everything to left is smaller. everything to right is bigger.

C A C H A B E C [K] O L R O S

C is next iteration. (why?)

A A B [C] C C E H K O L R O S

O is next (why?)

A A B C C C E H K L [O] O R S

Array is sorted but still have to go over any pivots not gone thru yet. For sure R and S will run and be in the correct spot already

A A B C C C E H K L O O R S


4.  #### Quicksort 3-way (No Shuffle)

while i <= gt

Let v be partitioning item a[lo].
– (a[i] < v): exchange a[lt] with a[i];increment both lt and i
– (a[i] > v): exchange a[gt] with a[i]; decrement gt
– (a[i] == v): increment i

C O A C H A B L E R O C K S

C  S  A  C  H  A  B  L  E  R  O  C  K  O
lt i                                gt

C  K  A  C  H  A  B  L  E  R  O  C  S  O
lt i                            gt

C  C  A  C  H  A  B  L  E  R  O  K  S  O
lt i                         gt

C  C  A  C  H  A  B  L  E  R  O  K  S  O
lt    i                      gt

A  C  C  C  H  A  B  L  E  R  O  K  S  O
   lt    i                    gt

A  C  C  C  H  A  B  L  E  R  O  K  S  O
   lt    i                    gt

A  C  C  C  H  A  B  L  E  R  O  K  S  O
   lt       i                 gt

do 4 operations to get to next one:

A  C  C  C  L  A  B  E  R  O  H  K  S  O
   lt       i     gt

A  C  C  C  B  A  L  E  R  O  H  K  S  O
   lt       i  gt

A  B  C  C  C  A  L  E  R  O  H  K  S  O
      lt       gt
               i

A  B  A  C  C  C  L  E  R  O  H  K  S  O
         lt    gt 
                  i


##### now do Left for:
low (0) to lt - 1 (2)
A   B   A

A  A  B
lt gt
   i

A  A  B
lt gt
      i

##### do Right for:
gt+1 (6) to len-1 (13)

L  E  R  O  H  K  S  O
lt i                 gt

E  L  R  O  H  K  S  O
   lt i              gt

3 operations later:

E  L  K  O  H  S  O  R
   lt i     gt

E  K  L  O  H  S  O  R
      lt i  gt

E  K  L   H  O  S  O  R
      lt  gt
          i  

E  K  H  L  O  S  O  R
         gt
         lt i

I believe now it can go right again for:
gt+1 (10) to len-1 (13)

O   S   O   R
lt  i       gt
         
O   R   O   S
lt  i   gt

O   O   R   S
lt  gt
    i

5.  #### Mergesort Bottom Up

C O A C H A B L E R O C K S

###### L side
C O
A C
A C C O

A H
B
A B H

A A B C C H O

##### R side

E L
O R
E L O R

C K
S
C K S

C E K L O R S

--

A A B C C H O
C E K L O R S

A A C C C B E C K O L R O S




6.  #### Mergesort Top Down

C O A C H A B L E R O C K S

C O
A C

A H
B

L E
R O

C K 
S
--

A C C O

A B H

E L O R

C K S
--

A A B C C H O 

C E K L O R S
--

A A C C C B E C K O L R O S



## ## Match Sorting Algorithms
Here is an array that we're trying to sort several different ways. We'll provide the intermediate sorting stage, and you'll need to determine which sorting algorithm was used. We'll give you the first one as an example.

For some of them, multiple algorithms might apply. List as many as you can.

### #### Initial and Sorted Input

(initial) [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]

(sorted)  [0, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 21, 24, 27]


### #### Intermediate Stages To Identify

a) [0, 2, 3, 4, 5, 21, 17, 10, 16, 7, 24, 8, 27, 6, 18, 15]

b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]

c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]

d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]


#### (a) Selection sort

Selection sort -- 5 outer loops in. the array 0,2,3,4, 5 contains the smallest elements of the array in order - they are in the final positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,4,5 in their original positions.



#### (b) Quick sort

Quick sort -- 7 is the partition. 6 numbers 2,0,4,6,5,3 are smaller than 7. 8 numbers 15,27,17,10,16,8,24,18 are greater



#### (c) Insertion sort

Insertion sort -- 12 outer loops in. All but last four items -- 4,6,18,5 have been sorted



#### (d) Merge sort

Merge sort -- More than half way done. There's four 4 item sorted sequences within the 16 items. 2 more sorts are left. Merge into 2 sorted sequences then one final sort.

